import os
from ultralytics import YOLO

os.system("cls||clear")

current_dir = os.path.dirname(os.path.realpath(__file__))
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data=f"{current_dir}/config.yaml", epochs=5)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format
#
