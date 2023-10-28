import os

d = os.path.join(os.getcwd(), 'dataset')

for i in os.listdir(os.path.join(d, 'video2', 'frames_rgb')):
    os.rename(os.path.join(d, 'video2', 'frames_rgb', i),
              os.path.join(d, 'video2', 'frames_rgb', f"{i.replace('video1_', '')}"))

# for i in os.listdir(os.path.join(d, 'images', 'val')):
#     os.rename(os.path.join(d, 'images', 'val', i),
#               os.path.join(d, 'images', 'val', f"video0_{i}"))

# for i in os.listdir(os.path.join(d, 'labels', 'train')):
#     os.rename(os.path.join(d, 'labels', 'train', i),
#               os.path.join(d, 'labels', 'train', f"video0_{i}"))

# for i in os.listdir(os.path.join(d, 'labels', 'val')):
#     os.rename(os.path.join(d, 'labels', 'val', i),
#               os.path.join(d, 'labels', 'val', f"video0_{i}"))
