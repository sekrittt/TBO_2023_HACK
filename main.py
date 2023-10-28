import os
from model.ai import Model
from argparse import ArgumentParser, Namespace
from collections import Counter

import boxcomparison as BC

from pprint import pprint

class App:
    def __init__(self, args: Namespace):
        self.current_dir = os.getcwd()
        self.model = Model()
        file_result = 'frame,wood,glass,plastic,metal'
        classes = ["wood", "glass", "plastic", "metals"]
        if args.train:
            self.model.train(100, self.current_dir)
        else:
            self.model.load(os.path.join(self.current_dir, 'model-m.pt'))

        results = [*zip(self.model.process(
            [os.path.join(args.input, img) for img in os.listdir(args.input)]), os.listdir(args.input))]

        prev_frame = []
        differences = {"wood": 0, "plastic": 0, "glass": 0, "metals": 0}
        delta, direction, coord = 0, 0, ''
        calced_consts = False
        for i, [result, img] in enumerate(results):
            if result.boxes is not None:
                frame = []
                # frame = [["wood","plastic"],
                #          [[1,2,3,4],[3,45,5,5]]]
                frame.append([classes[int(i)] for i in result.boxes.cls])
                frame.extend([[[int(h) for h in list(j)] for j in list(b.xyxy)]
                             for b in result.boxes])

                if not calced_consts and i > 0:
                    delta = BC.find_delta(prev_frame, frame)
                    direction, coord = BC.find_direction(prev_frame, frame)
                    calced_consts = True

                if calced_consts:
                    n_differences = BC.counter(
                        prev_frame, frame, delta, direction, coord)
                    differences["glass"] += n_differences["glass"]
                    differences["plastic"] += n_differences["plastic"]
                    differences["metals"] += n_differences["metals"]
                    differences["wood"] += n_differences["wood"]

                # For CSV
                res_classes = {**{k: 0 for k in classes}, **
                               dict(Counter([classes[int(i)] for i in result.boxes.cls]))}
                file_result += f'\n{img.replace(".png", "")[7:]},{res_classes["wood"]},{res_classes["glass"]},{res_classes["plastic"]},{res_classes["metal"]}'
                prev_frame = [*frame]
        pprint(differences)

        with open(os.path.join(args.output, 'frames.csv'), 'w', encoding="utf-8") as f:
            f.write(file_result)

        # for img in os.listdir(args.input):
        #     img_pil = Image.open(os.path.join(args.input, img))
        #     res = self.model.process(img_pil)
        #     if res[0].boxes is not None:
        #         counter(res[0].boxes, [], 0)  # type: ignore
        #         return json.dumps({"success": True, "message": "Upload!", "image_url": f'/predict/{filename}', 'classes': dict(Counter([classes[int(i)] for i in res[0].boxes.cls]))})


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
