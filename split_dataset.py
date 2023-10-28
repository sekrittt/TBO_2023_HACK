import os
import random
import shutil

d = os.path.join(os.getcwd(), 'data', 'images', 'train')
d2 = os.path.join(os.getcwd(), 'data', 'images', 'val')
d_l = os.path.join(os.getcwd(), 'data', 'labels', 'train')
d2_l = os.path.join(os.getcwd(), 'data', 'labels', 'val')
d_list = os.listdir(d)

random.shuffle(d_list)

train_list = d_list[:round(len(d_list)*0.8)]
val_list = d_list[round(len(d_list)*0.8):]

for v in val_list:
    shutil.move(os.path.join(d, v), os.path.join(d2, v))
    shutil.move(os.path.join(d_l, v.replace(".png", ".txt")),
                os.path.join(d2_l, v.replace(".png", ".txt")))
