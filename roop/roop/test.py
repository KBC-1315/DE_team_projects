from fake_generator import *
import cv2

temp_image = cv2.imread("/home/tobe1315/my_projects/face_swapper/Deepfake/source/sample1.png")
print(temp_image)
temp = generate_fake(0 ,temp_image)