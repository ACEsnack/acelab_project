import cv2
import os, sys
import copy

file_path = "../gt20_image_depth_MonoDEVSNet/3.png"
save_path = "./1.png"
image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

img = copy.deepcopy(image)
print(len(img), len(img[0]))
for i in range(len(img)):
    for j in range(len(img[0])):
        if image[i][j] == 255:
            img = cv2.circle(img, (j, i), 2, 255, -1 )



cv2.imwrite(save_path,img)