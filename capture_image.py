import cv2
import os

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Get user input for registration number and name
reg_no = input("Enter registration number: ")
name = input("Enter name: ")

# Create a folder to store the captured images
folder_name = 'TrainingImages/' + reg_no + '_' + name
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Initialize variables for quality check
prev_size = 0
best_img = None

# Start capturing images
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Process the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Check if this face region is clearer than the previous one
        size = w * h
        if size > prev_size:
            prev_size = size
            best_img = gray[y:y+h, x:x+w]

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Wait for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save the clearest face image with registration number and name
cv2.imwrite(folder_name + '/' + reg_no + name + '.jpg', best_img)

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
