from fake_generator import *
import cv2

temp_image = cv2.imread("/home/tobe1315/my_projects/Face_swapper/source/IMG_3911.JPG")
print(temp_image)
temp = generate_fake("F" ,temp_image)