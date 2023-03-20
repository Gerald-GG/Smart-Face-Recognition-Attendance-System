import cv2
import os
import numpy as np
import pandas as pd
from datetime import datetime

# Disable OpenCL acceleration in OpenCV
cv2.ocl.setUseOpenCL(False)

# Create a face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the trained face recognizer from a file
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_recognizer.xml")

# Create attendance folder if it doesn't exist
if not os.path.exists("Attendance"):
    os.makedirs("Attendance")

# Create unknown folder if it doesn't exist
if not os.path.exists("unknown"):
    os.makedirs("unknown")

# Initialize attendance dataframe
attendance = pd.DataFrame(columns=["Name", "Time"])
attendance.index.name = "ID"

# Get the list of names from the TrainingImages subfolder
names = os.listdir("TrainingImages")

# Create a dictionary to map label values to names in TrainingImages subfolder
label_dict = {i: names[i] for i in range(len(names))}

# Define font for displaying text on video stream
font = cv2.FONT_HERSHEY_SIMPLEX

# Create a video capture object
cap = cv2.VideoCapture(0)

# Initialize total students count
total_students = 0

while True:
    # Read a frame from the video stream
    ret, img = cap.read()

    # Convert the frame to grayscale and detect faces
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Recognize faces and mark attendance or save unknown faces
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_roi)
        if confidence < 100:
            name = label_dict[label]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, name, (x, y-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            if label not in attendance.index:
                attendance.loc[label] = [name, datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")]
                total_students += 1
            else:
                attendance.loc[label]["Time"] = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
        else:
            unknown_filename = datetime.now().strftime("unknown_%A_%Y-%m-%d_%H-%M-%S.jpg")
            cv2.imwrite(os.path.join("unknown", unknown_filename), img[y:y+h, x:x+w])

    # Display the resulting image
    cv2.imshow("Recognizing faces for Attendance", img)

    # Quit the program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Add total students count to the attendance dataframe
attendance.loc["Total Students"] = ["", total_students]

# Save the attendance to a file named in today's day, date, and time
filename = datetime.now().strftime("attendance_%A_%Y-%m-%d_%H-%M-%S.xlsx")
attendance.to_excel(os.path.join("Attendance", filename))

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
