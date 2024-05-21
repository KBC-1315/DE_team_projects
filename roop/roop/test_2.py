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
test_image = cv2.imread("/home/tobe1315/my_projects/Face_swapper/source/sample4.jpg")
test = generate_fake("11111111111111", "F", test_image)
print(test)