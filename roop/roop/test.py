from fake_generator import *
import cv2

temp_image = cv2.imread("/home/tobe1315/my_projects/Face_swapper/source/sample1.png")
print(temp_image)
temp = generate_fake("F" ,temp_image)