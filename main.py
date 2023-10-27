from re import X
import tensorflow as tf
from tensorflow import keras
import os
from typing import Literal

image_height = 360
image_width = 640

current_dir = os.path.dirname(os.path.realpath(__file__))

def load_dataset(pathnumber: Literal[0, 1, 2]):#startpath = 0|1|2
    path_ms = f"{current_dir}/dataset/video{pathnumber}/frames_ms"
    path_output = f"{current_dir}/dataset/video{pathnumber}/frames_output"
    images = os.listdir(path_ms)
    txts = os.listdir(path_output)
    
    return 
    


model = keras.models.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(2, activation='softmax')  # 2 classes: MSW and Healthy
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10, validation_data=(val_images, val_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')


predictions = model.predict(new_images)
