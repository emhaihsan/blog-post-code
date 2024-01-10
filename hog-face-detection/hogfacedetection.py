import argparse
import dlib
import cv2

def detect_faces(image_path):
    # Load the pre-trained face detector from dlib
    detector = dlib.get_frontal_face_detector()

    # Load an image from file
    img = cv2.imread(image_path)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    # Draw rectangles around the faces
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow('Face Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Face detection on an image')

    # Add the image path argument
    parser.add_argument('image_path', type=str, nargs='?', default='./img/image1.png', 
                        help='Path to the input image (default: ./img/image1.png)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform face detection on the specified image
    detect_faces(args.image_path)
