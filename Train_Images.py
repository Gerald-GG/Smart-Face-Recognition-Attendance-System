import csv
import cv2
cv2.ocl.setUseOpenCL(False)
import os
import numpy as np

# Path to the folder containing the training images
folder_path = 'TrainingImages/'

# Create a face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Create a list to hold the face images and labels
faces = []
labels = []
reg_nos = []

# Create a dictionary to map label names to integer values
label_dict = {}

# Loop over the subfolders in the training images folder
for subfolder_name in os.listdir(folder_path):
    # Extract the label (name) from the subfolder name
    label_name = subfolder_name.split('_')[0]
    reg_no = subfolder_name.split('_')[1]
    
    # If this label hasn't been assigned an integer value yet, assign it one
    if label_name not in label_dict:
        label_dict[label_name] = len(label_dict)
    
    # Loop over the images in the subfolder
    for image_name in os.listdir(folder_path + subfolder_name):
        # Load the image
        image_path = folder_path + subfolder_name + '/' + image_name
        image = cv2.imread(image_path)
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        # Process each detected face
        for (x, y, w, h) in faces_rect:
            # Extract the face region of interest
            face_roi = gray[y:y+h, x:x+w]
            
            # Add the face ROI and label to the lists
            faces.append(face_roi)
            labels.append(label_dict[label_name])
            reg_nos.append(reg_no)

# Convert the labels and reg_nos lists to numpy arrays
labels_array = np.array(labels)
reg_nos_array = np.array(reg_nos)

# Train the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels_array)

# Save the trained face recognizer to a file
recognizer.save("face_recognizer.xml")

# Save the names and reg_nos arrays to a CSV file
with open('students.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Name', 'Reg_No']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for name, reg_no in zip(label_dict.keys(), reg_nos_array):
        writer.writerow({'Reg_No': reg_no, 'Name': name})
