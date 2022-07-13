import shutil
import os


path_dir = '../images'
 
file_list = os.listdir(path_dir)
file_list.sort()

total = len(file_list)

print(total)


if os.path.exists("new_img"):
    shutil.rmtree("new_img")

os.mkdir("new_img")

for i in range(2, total, 3):
    shutil.copy(path_dir+"/"+file_list[i], "./new_img")

