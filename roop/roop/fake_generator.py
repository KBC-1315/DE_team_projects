from roop import core
import argparse
import cv2
import dlib
import os
import time

def generate_unique_id() -> str:
    current_time = int(time.time() * 1000)
    return str(current_time)


def generate_fake(ID, gender_type, source_image) :
    if ID is not str :
        ID = str(ID)
    temp_id = ID + ".jpg"
    cv2.imwrite("/home/tobe1315/my_projects/Face_swapper/temp_source/" + temp_id, source_image)
    run_args = argparse.Namespace(
        source_path="/home/tobe1315/my_projects/Face_swapper/temp_source/{}".format(temp_id),
        target_path="/home/tobe1315/my_projects/Face_swapper/Background/Background/test.jpg",
        output_path="/home/tobe1315/my_projects/Face_swapper/{}/test_no.jpg".format(temp_id),
        frame_processor=["face_swapper", "face_enhancer"],  # 필요한 경우 추가 파라미터를 설정할 수 있습니다
        keep_fps=False,
        keep_frames=False,
        skip_audio=False,
        many_faces=False,
        reference_face_position=0,
        reference_frame_number=0,
        similar_face_distance=0.85,
        temp_frame_format="png",
        temp_frame_quality=0,
        output_video_encoder="libx264",
        output_video_quality=35,
        max_memory=None,
        execution_provider=["cuda"],
        execution_threads= 8,
        temp_id = ""
    )
    run_args.headless = True  # headless 모드로 실행하도록 설정합니다
    folder_path = r"/home/tobe1315/my_projects/Face_swapper/output/{}".format(temp_id.split(".")[0])
    os.mkdir(folder_path)
    core.bounding_boxes("/home/tobe1315/my_projects/Face_swapper/temp_source/" + temp_id, "/home/tobe1315/my_projects/Face_swapper/face_detection/" + temp_id)
    core.draw_landmarks("/home/tobe1315/my_projects/Face_swapper/temp_source/" + temp_id, "/home/tobe1315/my_projects/Face_swapper/face_landmarks/" + temp_id)
    run_args.temp_id = temp_id.split(".")[0]
    if gender_type == "M" :
        male_list = []
        for i in range(1, 7):
            run_args.target_path = "/home/tobe1315/my_projects/Face_swapper/Background/Background/MALE_{}.jpg".format(i)
            run_args.output_path = "/home/tobe1315/my_projects/Face_swapper/output/{}/{}".format(temp_id.split(".")[0],temp_id.split(".")[0] + "_MALE_{}.jpg".format(i))
            core.run(run_args)
            male_list.append(cv2.imread(run_args.output_path))
        return male_list
    elif gender_type == "F" :
        female_list = []
        for i in range(1, 7):
            run_args.target_path = "/home/tobe1315/my_projects/Face_swapper/Background/Background/test_{}.jpg".format(i)
            run_args.output_path = "/home/tobe1315/my_projects/Face_swapper/output/{}/{}".format(temp_id.split(".")[0],temp_id.split(".")[0] + "_FEMALE_{}.jpg".format(i))
            core.run(run_args)
            female_list.append(cv2.imread(run_args.output_path))
        return female_list
    else :
        output_list = []
        for i in range(1, 7):
            run_args.target_path = "/home/tobe1315/my_projects/Face_swapper/Background/Background/MALE_{}.jpg".format(i)
            run_args.output_path = "/home/tobe1315/my_projects/Face_swapper/output/{}/{}".format(temp_id.split(".")[0],temp_id.split(".")[0] + "_MALE_{}.jpg".format(i))
            core.run(run_args)
            male_list.append(cv2.imread(run_args.output_path))

        for i in range(1, 7):
            run_args.target_path = "/home/tobe1315/my_projects/Face_swapper/Background/Background/test_{}.jpg".format(i)
            run_args.output_path = "/home/tobe1315/my_projects/Face_swapper/output/{}/{}".format(temp_id.split(".")[0],temp_id.split(".")[0] + "_FEMALE_{}.jpg".format(i))
            core.run(run_args)
            female_list.append(cv2.imread(run_args.output_path))
        return output_list
    



    