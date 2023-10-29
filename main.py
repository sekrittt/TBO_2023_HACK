import os
from model.ai import Model
from argparse import ArgumentParser, Namespace
from collections import Counter

import boxcomparison as BC

from pprint import pprint


def split_input(inp: list):
    offset = 0
    for i in range((len(inp)//100)+1):
        if offset + 100 <= len(inp):
            yield offset, inp[offset:offset+100]
        else:
            yield offset, inp[offset:]
        offset += 100


class App:
    def __init__(self, args: Namespace):
        self.current_dir = os.getcwd()
        self.model = Model()
        file_result = 'frame_id;wood;glass;plastic;metal'
        classes = ["wood", "glass", "plastic", "metal"]
        if args.train:
            self.model.train(100, self.current_dir)
        else:
            self.model.load(os.path.join(self.current_dir, 'model-m.pt'))

        prev_frame = []
        differences = {"wood": 0, "plastic": 0, "glass": 0, "metal": 0}
        delta, direction, coord = 0, 0, ''
        calced_consts = False
        p_img = ''

        for offset, part in split_input(os.listdir(args.input)):
            results = [
                *zip(self.model.process([os.path.join(args.input, img) for img in part]), part)]

<<<<<<< Updated upstream
                if calced_consts:
                    n_differences = BC.counter(
                        prev_frame, frame, delta, direction, coord)
                    differences["glass"] += n_differences["glass"]
                    differences["plastic"] += n_differences["plastic"]
                    differences["metal"] += n_differences["metal"]
                    differences["wood"] += n_differences["wood"]
                if i == len(results)-1:
                    n_d = BC.find_all(frame)
                    differences["glass"] += n_d["glass"]
                    differences["plastic"] += n_d["plastic"]
                    differences["metal"] += n_d["metal"]
                    differences["wood"] += n_d["wood"]
=======
            for i, [result, img] in enumerate(results):
                if result.boxes is not None:
                    frame = [[classes[int(i)] for i in result.boxes.cls], []]
                    # frame = [["wood","plastic"],
                    #          [[1,2,3,4],[3,45,5,5]]]
>>>>>>> Stashed changes

                    for b in result.boxes:
                        frame[1].extend([*map(lambda x: [float(h)
                                        for h in x], list(b.xyxy))])

                    # print(result.boxes)
                    if offset+i > 0:
                        find_delta = BC.find_delta(os.path.join(os.getcwd(),
                                                                args.input, p_img), os.path.join(os.getcwd(), args.input, img))
                        # print(offset, i, offset+i)
                        delta *= offset+i-1
                        delta = delta+find_delta
                        delta /= offset+i
                        print(delta)

                    # print(delta)
                    if not calced_consts and i > 0:

                        direction, coord = BC.find_direction(prev_frame, frame)
                        calced_consts = True

                    if calced_consts:
                        n_differences = BC.counter(
                            prev_frame, frame, delta, direction, coord)
                        differences["glass"] += n_differences["glass"]
                        differences["plastic"] += n_differences["plastic"]
                        differences["metal"] += n_differences["metal"]
                        differences["wood"] += n_differences["wood"]
                    if i == len(results)-1:
                        n_d = BC.find_all(frame)
                        differences["glass"] += n_d["glass"]
                        differences["plastic"] += n_d["plastic"]
                        differences["metal"] += n_d["metal"]
                        differences["wood"] += n_d["wood"]

                    # For CSV
                    res_classes = {**{k: 0 for k in classes}, **
                                   dict(Counter([classes[int(i)] for i in result.boxes.cls]))}
                    file_result += f'\nf{int(img.replace(".png", ""))};{res_classes["wood"]};{res_classes["glass"]};{res_classes["plastic"]};{res_classes["metal"]}'
                    prev_frame = frame
                    p_img = img
        pprint(differences)

        file_result += f'\nf_all;{differences["wood"]};{differences["glass"]};{differences["plastic"]};{differences["metal"]}'

        with open(os.path.join(args.output, 'frames.csv'), 'w', encoding="utf-8") as f:
            f.write(file_result)


if __name__ == "__main__":
    os.system("cls||clear")
    parser = ArgumentParser(prog="tbo_detector")
    parser.add_argument('--input', type=str, help="Data for process")
    parser.add_argument('--output', type=str, help="Processed data")
    parser.add_argument('--train', type=bool,
                        default=False, help="Training model")

    args = parser.parse_args()

    if not args.train:
        if not os.path.exists(args.input):
            print(f"Path '{args.input}' not exists!")
            exit(1)
        if not os.path.isdir(args.input):
            print(f"'{args.input}' isn't directory ")
            exit(1)
        if not os.path.exists(args.output):
            print(f"Path '{args.output}' not exists!")
            exit(1)
        if not os.path.isdir(args.output):
            print(f"'{args.output}' isn't directory ")
            exit(1)
    App(args)
