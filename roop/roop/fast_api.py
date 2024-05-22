from fake_generator import *
import cv2
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import cv2
import numpy as np
import os
import time
from typing import List
from roop import core
import argparse
import pathlib
<<<<<<< HEAD
import psutil
import subprocess
import json
import base64

def get_gpu_info():
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=index,name,utilization.gpu,memory.total,memory.used,memory.free', '--format=csv,noheader,nounits'], capture_output=True)
        gpu_info = result.stdout.decode('utf-8').strip().split('\n')
        gpu_info_list = []
        for gpu in gpu_info:
            gpu_info_list.append(dict(zip(['index', 'name', 'gpu_utilization', 'memory_total', 'memory_used', 'memory_free'], gpu.split(','))))
        return gpu_info_list
    except Exception as e:
        print(f"Error fetching GPU info: {e}")
        return "Not available"
app = FastAPI()

@app.get("/getBoundbox/")
async def get_Boundboxes(ID: str):
    try:
        temp_ID = ID
        image_path = f"/home/tobe1315/my_projects/Face_swapper/face_detection/{temp_ID}.jpg"
        
        # 이미지 파일을 읽어옴
        source_image = cv2.imread(image_path)
        
        if source_image is None:
            return JSONResponse(content={"error": "Could not find image"}, status_code=400)
        
        # 이미지를 JPEG로 인코딩
        _, buffer = cv2.imencode(".jpg", source_image)
        
        # base64로 인코딩
        encoded_image = base64.b64encode(buffer).decode("utf-8")
        
        return JSONResponse(content={"image": encoded_image})
    except :
        return JSONResponse(content={"error": "Could not find image"}, status_code=400)


@app.get("/getLandmarks/")
def get_Landmarks(ID: int):
    try:
        ID = str(ID)
        image_path = f"/home/tobe1315/my_projects/Face_swapper/face_landmarks/{ID}.jpg"
        print(image_path)
        file = cv2.imread(image_path)
        
        if file is None:
            return JSONResponse(content={"error": "Could not find image"}, status_code=400)

        _, buffer = cv2.imencode(".jpg", file)
        encoded_image = base64.b64encode(buffer).decode("utf-8")

        return JSONResponse(content={"image": encoded_image})
    
    except Exception as e:
        return JSONResponse(content={"error": "An error occurred", "details": str(e)}, status_code=400)

@app.get("/getLowResolution/")
def get_Low_Resolution(ID: int):
    try:
        ID = str(ID)
        result_images = []
        file_path = f"/home/tobe1315/my_projects/Face_swapper/face_swapper/{ID}/"
        
        for file in os.listdir(file_path):
            image = cv2.imread(os.path.join(file_path, file))
            if image is not None:
                result_images.append(image)

        # 이미지들을 base64로 인코딩하여 리스트로 반환
        encoded_images = []
        for image in result_images:
            _, buffer = cv2.imencode('.jpg', image)
            encoded_image = base64.b64encode(buffer).decode('utf-8')
            encoded_images.append(encoded_image)

        return JSONResponse(content={"images": encoded_images})
    
    except Exception as e:
        return JSONResponse(content={"error": "An error occurred", "details": str(e)}, status_code=400)

@app.get("/system-info")
async def get_system_info():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        gpu_info = get_gpu_info()  # GPU 정보 수집 코드 추가 필요 (예: GPUtil 라이브러리)

        system_info = {
            "cpu_usage_percent": cpu_usage,
            "memory_total": memory.total,
            "memory_used": memory.used,
            "memory_percent": memory.percent,
            "gpu_info": gpu_info
        }

        return JSONResponse(content=system_info)
    
    except Exception as e:
        return JSONResponse(content={"error": "An error occurred", "details": str(e)}, status_code=400)



@app.post("/fakeface/")
async def create_fake_images(ID: int, gender_type: str, file: UploadFile = File(...)):
=======
import base64

app = FastAPI()

@app.post("/fakeface/")
async def create_fake_images(gender_type: str, file: UploadFile = File(...)):
>>>>>>> 841f54f39e63c843d9fc34e4380976e953c65d6a
    try:
        file_contents = await file.read()
        nparr = np.frombuffer(file_contents, np.uint8)
        source_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if source_image is None:
            return JSONResponse(content={"error": "Could not decode image"}, status_code=400)

<<<<<<< HEAD
        result_images = generate_fake(ID, gender_type, source_image)
=======
        result_images = generate_fake(gender_type, source_image)
>>>>>>> 841f54f39e63c843d9fc34e4380976e953c65d6a

        # 이미지들을 base64로 인코딩하여 리스트로 반환
        encoded_images = []
        for image in result_images:
            _, buffer = cv2.imencode('.jpg', image)
            encoded_image = base64.b64encode(buffer).decode('utf-8')
            encoded_images.append(encoded_image)

        return JSONResponse(content={"images": encoded_images})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)