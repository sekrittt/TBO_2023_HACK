import cv2
import numpy as np


def find_delta(p_img, n_img):

    image1 = cv2.imread(p_img)
    image2 = cv2.imread(n_img)

    if image1 is None or image2 is None:
        raise Exception("Не удалось загрузить изображения")

    # Преобразование изображений в оттенки серого
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Вычисление оптического потока с использованием Lucas-Kanade
    lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(
        cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    prevPts = cv2.goodFeaturesToTrack(
        image1_gray, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    p1, st, err = cv2.calcOpticalFlowPyrLK(
        image1_gray, image2_gray, prevPts, None, **lk_params)

    if p1 is not None:
        # Вычисление среднего смещения
        displacement = np.mean(p1 - prevPts, axis=0)
        return displacement[0][0]*1.65

    return None


# подсчет расстояния между боксами
def find_distance(box_first: list, box_second: list) -> float:
    return ((box_first[2]-box_second[0])**2 +
            (box_first[3]-box_second[1])**2)**0.5


# подсчет отличий(новых объектов) в массиве
def counter(frame_first: list, frame_second: list, delta: float, direction: float, dir_coord: str) -> dict:
    differences = {"wood": 0, "plastic": 0, "glass": 0, "metal": 0}
    for first_number in range(len(frame_first[1])):
        for second_number in range(len(frame_second[1])):
            if find_distance(frame_first[1][first_number], frame_second[1][second_number]) < delta:
                break
            else:
                if dir_coord == 'x':
                    # print(frame_first[1][first_number])
                    if (direction-abs(frame_first[1][first_number][0]) < delta):
                        differences[frame_first[0][first_number]] += 1
                        break
                else:
                    if (abs(direction-frame_first[1][first_number][1]) < delta):
                        differences[frame_first[0][first_number]] += 1
                        break

    return differences

def find_all(frame: list) -> dict:
    differences = {"wood": 0, "plastic": 0, "glass": 0, "metal": 0}
    for item in frame[0]:
        differences[item]+=1
    return differences

def find_direction(frame_first: list, frame_second: list, coords_start_x: float = 0, coords_end_x: float = 640,
                   coords_start_y: float = 0, coords_end_y: float = 360) -> tuple[float, str]:
    # сюда передаем корды х первого бокса и второго бокса
    mas = []
    for box_first in frame_first[1]:
        for box_second in frame_second[1]:
            mas.append([box_first[0]-box_second[0],
                       box_first[1]-box_second[1]])
    x, y = 0, 0
    for coords in mas:
        x += coords[0]
        y += coords[1]
    x /= len(mas)
    y /= len(mas)
    if abs(x) > abs(y):
        direction = coords_end_x if x < 0 else coords_start_x
        coord = "x"
    else:
        direction = coords_end_y if y < 0 else coords_start_y
        coord = "y"
    return direction, coord


def find_all(frame: list) -> dict:
    differences = {"wood": 0, "plastic": 0, "glass": 0, "metal": 0}
    for item in frame[0]:
        differences[item] += 1
    return differences
