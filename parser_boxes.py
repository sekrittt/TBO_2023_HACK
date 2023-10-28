import os
from typing import Union
from pprint import pprint

current_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_dir, "dataset", "video0", "video0.txt"), 'r', encoding="utf-8") as f:
    data_list = [[float(j.strip()) if '.' in j else int(j.strip()) for j in i.strip().split(",")] for i in f]
    data_dict: dict[str, list[list[Union[float, int]]]] = {}
    objects_id: list[Union[float, int]] = []
    for i in data_list:
        if f'{i[0]}'.rjust(4, '0') in data_dict:
            data_dict[f'{i[0]}'.rjust(4, '0')].append(i[2:])
        else:
            data_dict[f'{i[0]}'.rjust(4, '0')] = [i[2:]]
        objects_id.append(i[1])
    # for num, data in data_dict.items():
    #     file_name = f'{num}.txt'
    #     with open(os.path.join(current_dir, "data", "labels", "train", file_name), "w", encoding="utf-8") as f:
    #         f.write('\n'.join([' '.join([str(j) for j in i]) for i in data]))
    print(sorted([*set(objects_id)]))
