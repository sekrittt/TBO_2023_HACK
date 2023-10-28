from PIL import Image
import numpy as np


def is_full_new_image(prev_image: str, current_image: str):
    pi = Image.open(prev_image)
    ci = Image.open(current_image)

    pil: list[list[list[int]]] = []
    cil: list[list[list[int]]] = []

    pid = list(pi.getdata())
    for h in range(pi.height):
        pil.append([])
        for w in range(pi.width):
            pil[-1].append(pid[h*pi.height + w])

    cid = list(ci.getdata())
    for h1 in range(ci.height):
        cil.append([])
        for w1 in range(ci.width):
            cil[-1].append(cid[h1*ci.height + w1])

    return np.array(cid) | np.array(pid)


print(is_full_new_image('./data/images/train/video0_0002.png',
                        './data/images/train/video1_0015.png'))

# img = Image.open('./video0_0002.png')

# l = []

# for i in list(img.getdata()):
#     l.extend(i)

# print(set(l))
