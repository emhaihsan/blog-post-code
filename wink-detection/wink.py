import cv2
import dlib
import numpy as np

# Load the pre-trained face detector and shape predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize video capture
cap = cv2.VideoCapture(0)

# Define the wink detection parameters
EAR_THRESHOLD = 0.19
WINK_CONSEC_FRAMES = 3

# Initialize wink counter
wink_counter = 0

def eye_aspect_ratio(eye):
    # Calculate the Euclidean distances between the two sets of vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Calculate the Euclidean distance between the horizontal eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    return ear

def detect_wink(landmarks):
    left_eye = landmarks[36:42]
    right_eye = landmarks[42:48]

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    # Average the eye aspect ratio for both eyes
    avg_ear = (left_ear + right_ear) / 2.0

    return avg_ear

# Main loop
while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        # Detect landmarks in the face region
        landmarks = predictor(gray, face)

        # Convert landmarks to numpy array
        landmarks = np.array([[point.x, point.y] for point in landmarks.parts()])

        # Draw landmarks on the frame
        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        # Detect wink
        ear = detect_wink(landmarks)

        if ear < EAR_THRESHOLD:
            wink_counter += 1


    # Display the wink counter on the frame
    cv2.putText(frame, f"Total Winks: {wink_counter}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("Wink Detection", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
