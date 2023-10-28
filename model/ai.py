from ultralytics import YOLO
import os
from ultralytics.engine.results import Results

import shutil


class Model:
    def __init__(self, device='cuda') -> None:
        self.model = YOLO("yolov8s.yaml")
        self.model.to(device)
        # self.model.fuse()
        self.device = device

    def train(self, epochs, current_dir, auto_save=True):
        print("Model training...")
        self.model.train(data=os.path.join(
            current_dir, "config.yaml"), epochs=epochs)  # train the model
        print("Model trained!")
        if auto_save:
            self.save(os.path.join(current_dir, 'model.pt'))

    def save(self, path2save):
        print(f"Model saving...")
        d = os.path.join(os.getcwd(), 'runs', 'detect')
        folder: str = sorted([[i, os.stat(os.path.join(d, i)).st_mtime] for i in os.listdir(
            d) if 'train' in i], key=lambda x: x[1])[-1][0]  # type: ignore
        shutil.move(os.path.join(d, folder, 'weights', 'best.pt'), path2save)
        print(f"Model saved to {path2save}!")

    def process(self, source) -> list[Results]:
        print("Processing...")
        if os.path.exists(os.path.join(os.getcwd(), 'model', 'predict')):
            shutil.rmtree(os.path.join(os.getcwd(), 'model', 'predict'))
        result = self.model.predict(
            source=source, save=True, project="model", save_dir=os.path.join(os.getcwd(), 'results'))
        print("End processing!")
        return result

    def load(self, path2model):
        print(f"Model loading...")
        self.model = YOLO(path2model)
        self.model.to(self.device)
        # self.model.fuse()
        print(f"Model loaded from {path2model}!")
