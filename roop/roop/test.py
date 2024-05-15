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
import base64

app = FastAPI()

@app.post("/fakeface/")
async def create_fake_images(gender_type: str, file: UploadFile = File(...)):
    try:
        file_contents = await file.read()
        nparr = np.frombuffer(file_contents, np.uint8)
        source_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if source_image is None:
            return JSONResponse(content={"error": "Could not decode image"}, status_code=400)

        result_images = generate_fake(gender_type, source_image)

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