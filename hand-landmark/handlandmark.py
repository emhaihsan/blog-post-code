# import cv2
# import mediapipe as mp

# def detect_hand_landmarks(image, hands):
#     # Convert BGR image to RGB
#     mp_hands = mp.solutions.hands
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image
#     results = hands.process(image_rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             for landmark in hand_landmarks.landmark:
#                 h, w, _ = image.shape
#                 cx, cy = int(landmark.x * w), int(landmark.y * h)
#                 cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)

#         # Connect hand landmarks with lines
#         for hand_landmarks in results.multi_hand_landmarks:
#             for connection in mp_hands.HAND_CONNECTIONS:
#                 point1 = connection[0]
#                 point2 = connection[1]
#                 x1, y1 = int(hand_landmarks.landmark[point1].x * w), int(hand_landmarks.landmark[point1].y * h)
#                 x2, y2 = int(hand_landmarks.landmark[point2].x * w), int(hand_landmarks.landmark[point2].y * h)
#                 cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#     return image

# def detect_face_landmarks(image, face_mesh):
#     # Convert BGR image to RGB
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image
#     results = face_mesh.process(image_rgb)

#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             for landmark in face_landmarks.landmark:
#                 h, w, _ = image.shape
#                 cx, cy = int(landmark.x * w), int(landmark.y * h)
#                 cv2.circle(image, (cx, cy), 2, (0, 255, 0), -1)

#     return image

# def main():
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands()

#     mp_face_mesh = mp.solutions.face_mesh
#     face_mesh = mp_face_mesh.FaceMesh()

#     cap = cv2.VideoCapture(0)  # Use 0 for the default camera

#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Detect hand landmarks
#         frame = detect_hand_landmarks(frame, hands)

#         # Detect face landmarks
#         frame = detect_face_landmarks(frame, face_mesh)

#         # Display the frame
#         cv2.imshow("Hand and Face Landmarks", frame)

#         if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

import cv2
import mediapipe as mp

def detect_landmarks(image, hands, face_mesh):
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    hand_results = hands.process(image_rgb)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                h, w, _ = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)

            # Connect hand landmarks with lines
            for connection in mp.solutions.hands.HAND_CONNECTIONS:
                point1 = connection[0]
                point2 = connection[1]
                x1, y1 = int(hand_landmarks.landmark[point1].x * w), int(hand_landmarks.landmark[point1].y * h)
                x2, y2 = int(hand_landmarks.landmark[point2].x * w), int(hand_landmarks.landmark[point2].y * h)
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Process face landmarks
    face_results = face_mesh.process(image_rgb)
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                h, w, _ = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (cx, cy), 2, (0, 255, 0), -1)

    return image

def main():
    mp_hands = mp.solutions.hands.Hands()
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh()

    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Detect and draw hand and face landmarks
        frame = detect_landmarks(frame, mp_hands, mp_face_mesh)

        # Display the frame
        cv2.imshow("Hand and Face Landmarks", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
