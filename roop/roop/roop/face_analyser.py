import threading
from typing import Any, Optional, List
import insightface
import numpy
import cv2
import os

import roop.globals
from roop.typing import Frame, Face

FACE_ANALYSER = None
THREAD_LOCK = threading.Lock()

OUTPUT_DIR_1 = "/home/tobe1315/my_projects/Face_swapper/face_detection"
OUTPUT_DIR_2 = "/home/tobe1315/my_projects/Face_swapper/face_landmarks"
# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(OUTPUT_DIR_1):
    os.makedirs(OUTPUT_DIR_1)

if not os.path.exists(OUTPUT_DIR_2):
    os.makedirs(OUTPUT_DIR_2)    


def draw_bounding_boxes(image: Frame, faces: List[Face]) -> Frame:
    for face in faces:
        bbox = face.bbox.astype(int)
        x1, y1, x2, y2 = bbox
        # 얼굴 경계 상자 그리기
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return image

def draw_landmarks(image: Frame, faces: List[Face]) -> Frame:
    for face in faces:
        # 특징점 그리기
        for landmark in face.landmark.astype(int):
            cv2.circle(image, tuple(landmark), 2, (0, 0, 255), -1)
    return image

def save_image(filename: str, image: numpy.ndarray) -> None:
    filepath = os.path.join(OUTPUT_DIR, filename)
    cv2.imwrite(filepath, image)

def get_face_analyser() -> Any:
    global FACE_ANALYSER

    with THREAD_LOCK:
        if FACE_ANALYSER is None:
            FACE_ANALYSER = insightface.app.FaceAnalysis(name='buffalo_l', providers=roop.globals.execution_providers)
            FACE_ANALYSER.prepare(ctx_id=0)
    return FACE_ANALYSER


def clear_face_analyser() -> Any:
    global FACE_ANALYSER

    FACE_ANALYSER = None


def get_one_face(frame: Frame, position: int = 0) -> Optional[Face]:
    many_faces = get_many_faces(frame)
    if many_faces:
        try:
            return many_faces[position]
        except IndexError:
            return many_faces[-1]
    return None


def get_many_faces(frame: Frame) -> Optional[List[Face]]:
    try:
        #faces = get_face_analyser().get(frame)
        return get_face_analyser().get(frame)
    except ValueError:
        return None


def find_similar_face(frame: Frame, reference_face: Face) -> Optional[Face]:
    many_faces = get_many_faces(frame)
    if many_faces:
        for face in many_faces:
            if hasattr(face, 'normed_embedding') and hasattr(reference_face, 'normed_embedding'):
                distance = numpy.sum(numpy.square(face.normed_embedding - reference_face.normed_embedding))
                if distance < roop.globals.similar_face_distance:
                    return face
    return None
