
# pip install opencv-python
import cv2
import os

# Directory containing your image frames
input_directory = 'dataset/video1/frames_rgb'

# Output video file name
output_video = 'output.mp4'

# Get the list of image files in the input directory
image_files = [os.path.join(input_directory, f) for f in os.listdir(
    input_directory) if f.endswith(('.jpg', '.png'))]
image_files.sort()  # Sort the files in the correct order

# Get the first image to determine the video size
first_image = cv2.imread(image_files[0])
height, width, layers = first_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter.fourcc(*'mp4v')  # You can change the codec if needed
# Change the frame rate (30) if needed
out = cv2.VideoWriter(output_video, fourcc, 30, (width, height))

# Write each image to the video
for image_file in image_files:
    frame = cv2.imread(image_file)
    out.write(frame)

# Release the VideoWriter
out.release()

print(f'Video saved as {output_video}')
