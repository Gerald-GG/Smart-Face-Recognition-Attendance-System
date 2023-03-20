import cv2
import time

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a student detection classifier
student_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Set font and feedback message
font = cv2.FONT_HERSHEY_SIMPLEX
feedback_msg = 'No students detected'

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect students in the image
    students = student_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Get total number of students
    total_students = len(students)

    # Draw rectangles around the detected students and display the total number of students
    for (x, y, w, h) in students:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, f'Total Students: {total_students}', (10, 30), font, 1, (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('frame', frame)

    # Check if any students were detected and update the feedback message
    if total_students == 0:
        feedback_msg = 'No students detected'
    elif total_students == 1:
        feedback_msg = '1 student detected'
    else:
        feedback_msg = f'{total_students} students detected'

    # Display the feedback message
    cv2.putText(frame, feedback_msg, (10, frame.shape[0]-10), font, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)

    # Wait for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
