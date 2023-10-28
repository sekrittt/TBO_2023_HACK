from ultralytics import YOLO
import os
from ultralytics.engine.results import Results

import shutil


class Model:
    def __init__(self) -> None:
        self.model = YOLO("yolov8s.yaml")
        self.model.to('cuda')

    def train(self, epochs, current_dir, auto_save=True):
        print("Model training...")
        self.model.train(data=os.path.join(
            current_dir, "config.yaml"), epochs=epochs)  # train the model
        print("Model trained!")
        if auto_save:
            self.save(os.path.join(current_dir, 'model.pt'))

    def save(self, path2save):
        print(f"Model saving...")

        print(f"Model saved to {path2save}!")

    def process(self, source) -> list[Results]:
        print("Processing...")
        shutil.rmtree(os.path.join(os.getcwd(), 'ai', 'predict'))
        result = self.model.predict(
            source=source, save=True, project="ai", save_dir=os.path.join(os.getcwd(), 'results'))
        print("End processing!")
        return result

    def load(self, path2model):
        print(f"Model loading...")
        self.model = YOLO(path2model)
        self.model.to('cuda')
        print(f"Model loaded from {path2model}!")
