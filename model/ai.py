from ultralytics import YOLO

class Model:
    def __init__(self) -> None:
        self.model = YOLO("yolov8n.yaml")

    def train(self, epochs, current_dir):
        self.model.train(data=f"{current_dir}/config.yaml", epochs=epochs)  # train the model
    def save(self, current_dir):
        # self.model.export ?
        ...
