import cv2
import numpy as np
import requests
import os

# this program takes the video of the girl complaining about ice cream and draws green squares around the faces in the video.
# URLs for the required files
PROTOTXT_URL = "https://github.com/opencv/opencv/raw/master/samples/dnn/face_detector/deploy.prototxt"
MODEL_URL = "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"
VIDEO_URL = "https://tl-tefl.s3.us-west-2.amazonaws.com/videos/girl_complains_about_price_of_ice_cream.mp4"

# Download the required files
def download_files():
    # Create a directory to save the files
    model_dir = "face_detection_models"
    os.makedirs(model_dir, exist_ok=True)

    # Download the prototxt file
    prototxt_path = os.path.join(model_dir, "deploy.prototxt")
    if not os.path.exists(prototxt_path):
        print(f"Downloading {PROTOTXT_URL} to {prototxt_path}")
        with open(prototxt_path, "wb") as f:
            f.write(requests.get(PROTOTXT_URL).content)

    # Download the caffemodel file
    model_path = os.path.join(model_dir, "res10_300x300_ssd_iter_140000.caffemodel")
    if not os.path.exists(model_path):
        print(f"Downloading {MODEL_URL} to {model_path}")
        with open(model_path, "wb") as f:
            f.write(requests.get(MODEL_URL).content)

    # Download the video file
    video_path = os.path.join(model_dir, "girl_complains_about_price_of_ice_cream.mp4")
    if not os.path.exists(video_path):
        print(f"Downloading {VIDEO_URL} to {video_path}")
        with open(video_path, "wb") as f:
            f.write(requests.get(VIDEO_URL).content)

    return prototxt_path, model_path, video_path

# Download the required files
PROTOTXT_PATH, MODEL_PATH, VIDEO_PATH = download_files()

# Load the DNN face detection model
net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, MODEL_PATH)

# Open the video capture
cap = cv2.VideoCapture(VIDEO_PATH)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Get the frame dimensions
    (h, w) = frame.shape[:2]

    # Create a blob from the frame
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    # Pass the blob through the network and get the detections
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(0, detections.shape[2]):
        # Extract the confidence and bounding box coordinates
        confidence = detections[0, 0, i, 2]
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # Filter out weak detections and small faces
        if confidence > 0.5 and (endX - startX) > 100 and (endY - startY) > 100:
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()