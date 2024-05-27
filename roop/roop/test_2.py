from fake_generator import *
import cv2
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import cv2
import numpy as np
import os
import time
from tqdm.auto import tqdm
from typing import List
from roop import core
import argparse
import pathlib
import base64
folder_path = "/home/tobe1315/my_projects/Face_swapper/temp_source"
png_files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.jpg')]
for i in tqdm(png_files) :
    temp_img = cv2.imread(folder_path + "/" + i)
    test = generate_fake(i, "F", temp_img)
    test = generate_fake(i, "M", temp_img)    