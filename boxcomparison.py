def find_delta(frame_first: list, frame_second: list) -> float:
    mas = [10**10, 10**10]
    deltas = []
    for box_first in frame_first[1]:
        for box_second in frame_second[1]:
            mas[0] = min(abs(box_first[0]-box_second[0]), mas[0])  # x
            mas[1] = min(abs(box_first[1]-box_second[1]), mas[1])  # y
        deltas.append(mas)
    sumx, sumy = 0, 0
    for x, y in deltas:
        sumx += x
        sumy += y
    sumx = sumx/len(deltas)
    sumy = sumy/len(deltas)
    return (sumx**2+sumy**2)**0.5*1.1  # погрешность


# подсчет расстояния между боксами
def find_distance(box_first: list, box_second: list) -> float:
    return ((box_first[0]+box_first[2]-box_second[0]-box_second[2])**2 +
            (box_first[1]+box_first[3]-box_second[1]-box_second[3])**2)**0.5


# подсчет отличий(новых объектов) в массиве
def counter(frame_first: list, frame_second: list, delta: float, direction: float, dir_coord: str) -> dict:
    differences = {"wood": 0, "plastic": 0, "glass": 0, "metal": 0}
    for first_number in range(len(frame_first[1])):
        for second_number in range(len(frame_second[1])):
            if find_distance(frame_first[1][first_number], frame_second[1][second_number]) < delta:
                break
            else:
                if dir_coord == 'x':
                    if (abs(direction-frame_first[1][first_number][0]) < delta):
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

# Сначала вызвать find_delta и передать ей первый и второй фрейм, она вернет расстояние, которое проходит объект за фрейм
# можешь в цикле там пройтись, чтобы побольше значний получить и поделить их на кол-во(опционально)
# delta = find_delta()

# также find_direction() туда такие же параметры
# direction = find_direction()

# Затем вызвать first_count отдав туда первый фрейм, оно вернет кол-во объектов на фрейме

# Инициализировать переменную counter

# Потом по циклу со второго фрейма вызывать в цикле counter
