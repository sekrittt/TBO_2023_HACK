# from model.ai import Model
# import os
# from collections import Counter

# model = Model()
# model.load(os.path.join(os.getcwd(), 'model-m.pt'))

# res = model.model.predict('output.mp4', save=True)
# # print(res)

# classes = ["wood", "glass", "plastic", "metal"]
# # print({**{k: 0 for k in classes}, **dict(Counter([classes[int(i)] for i in res.boxes.cls]))})


# import cv2
# import numpy as np
# from yolo_v8 import load_yolo_model  # Replace with your YOLOv8 model loading code
# from sort import Sort  # Replace with SORT or DeepSORT tracking code

# # Load your YOLOv8 model
# yolo_model = load_yolo_model()

# # Initialize object tracker (using SORT in this example)
# tracker = Sort()

# # Load your video
# video_path = 'path_to_your_video.mp4'  # Replace with the path to your video
# cap = cv2.VideoCapture(video_path)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform object detection on the frame using YOLOv8
#     detections = yolo_model.detect(frame)  # Implement your YOLOv8 detection function

#     # Use the tracker to update object positions and IDs
#     trackers = tracker.update(detections)

#     for detection in trackers:
#         x, y, w, h, track_id = detection
#         class_name = yolo_model.classify(frame, x, y, x + w, y + h)  # Implement class prediction
#         # Classify and count objects based on class_name
#         if class_name == 'wood':
#             # Process wood object
#         elif class_name == 'plastic':
#             # Process plastic object
#         elif class_name == 'metal':
#             # Process metal object
#         elif class_name == 'glass':
#             # Process glass object

#     # Display or save the frame with tracked objects
#     # You can draw bounding boxes and labels on the frame to visualize object tracking

#     # Press 'q' to exit the loop if necessary
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release() Да заебало меня всё это уже сука блять пиздец нахуй, какого чёрта нихуя не работает бляяяяяяяяяяяяяяяяяяяяяя
# cv2.destroyAllWindows()

from model.ai import Model
from ultralytics.engine.results import Results

model = Model()
model.load('./model-m.pt')
res: list[Results] = model.model.track(
    ['./input/video1_0000.png', './input/video1_0001.png'], save=True, stream=True, show=True)

for r in res:
    if r.boxes is not None:
        print(r.boxes.id)
