import cv2
import os

# Directory where images are stored
image_folder = '/home/deepak/Desktop/29/ASS/VIDEO/IMAGES'

# Name of the output video file
video_name = 'TEST.mp4'

# Get all image filenames in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

# Sort images to ensure they are in the correct order
images.sort()

# Load the first image to get dimensions
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs like 'XVID'
fps=2
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))  # Set fps here

# Loop through the images and write them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# Release the video writer
video.release()

print(f'Video created: {video_name} at {fps} FPS')
