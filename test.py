# # from PIL import Image
# import os

# current_dir = os.path.dirname(os.path.realpath(__file__))
# # image = Image.open(f'{current_dir}/dataset/video0/frames_ms/0000.tif')
# # print(image.format, image.size, image.mode)
# from typing import Literal


# def splitset(arr):
#     kf = round(len(arr)*0.8)
#     trainarr = arr[0:kf]
#     testarr = arr[kf:]
#     return trainarr, testarr

# def load_dataset(pathnumber: Literal[0, 1, 2]):#startpath = 0|1|2
#     path_ms = f"{current_dir}/dataset/video{pathnumber}/frames_ms"
#     path_output = f"{current_dir}/dataset/video{pathnumber}/frames_output"
#     images = os.listdir(path_ms)
#     txts = os.listdir(path_output)
#     return splitset(images), splitset(txts)

# [img1,img2], [txt1,txt2] = load_dataset(1)
# print(len(txt1),len(txt2))

import os


# current_dir = os.path.dirname(os.path.realpath(__file__))

# with open(f"{current_dir}/dataset/video0/frames_output/0000.txt", 'r', encoding="utf-8") as f:
#     print([int(i.strip()) for i in f])

print(os.getcwd())
