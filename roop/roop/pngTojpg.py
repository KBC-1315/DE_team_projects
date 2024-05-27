from PIL import Image
import os

def convert_png_to_jpg(folder_path):
    # 폴더 안의 모든 파일 목록 얻기
    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith('.png'):
            # PNG 파일을 열고 JPG로 저장
            png_image = Image.open(os.path.join(folder_path, file))
            jpg_image_path = os.path.join(folder_path, os.path.splitext(file)[0] + '.jpg')
            png_image.save(jpg_image_path, 'JPEG')
            # 기존 PNG 파일 삭제 (원하는 경우)
            # os.remove(os.path.join(folder_path, file))
            print(f"{file} 변환 완료: {jpg_image_path}")
import os

def delete_png_files(folder_path):
    # 폴더 안의 모든 파일 목록 얻기
    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith('.png'):
            # PNG 파일 삭제
            os.remove(os.path.join(folder_path, file))
            print(f"{file} 삭제 완료")

# 삭제할 폴더 경로 설정
folder_path = '/home/tobe1315/my_projects/Face_swapper/temp_source'

# PNG 파일 삭제
delete_png_files(folder_path)

