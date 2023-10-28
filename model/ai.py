from ultralytics import YOLO
import torch
import os


class Model:
    def __init__(self) -> None:
        self.model = YOLO("yolov8n.yaml")

    def train(self, epochs, current_dir, auto_save=True):
        print("Model training...")
        self.model.train(data=os.path.join(
            current_dir, "config.yaml"), epochs=epochs)  # train the model
        print("Model trained!")
        if auto_save:
            self.save(os.path.join(current_dir, 'model.pt'))

    def save(self, path2save):
        print(f"Model saving...")
        torch.save(self.model.state_dict(), path2save)
        print(f"Model saved to {path2save}!")

    def process(self, source):
        print("Processing...")
        result = self.model.predict(source=source)
        print("End processing!")

    def load(self, path2model):
        print(f"Model loading...")
        self.model.load(weights=path2model)
        print(f"Model loaded from {path2model}!")
