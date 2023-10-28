from model.ai import Model
import os
from collections import Counter

model = Model()
model.load(os.path.join(os.getcwd(), 'model-m.pt'))

res = model.model.predict('output.mp4', save=True)
# print(res)

classes = ["wood", "glass", "plastic", "metal"]
# print({**{k: 0 for k in classes}, **dict(Counter([classes[int(i)] for i in res.boxes.cls]))})
