import os
import cv2

# Create a dictionary mapping numbers to letters (0-25 to A-Z)
LETTER_DICT = {i: chr(65 + i) for i in range(26)}  # 65 is ASCII for 'A'

# User configuration
USER_NAME = "daniel"  # Change this to your name
DATA_DIR = './data'

# Create main data directory
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_letters = 2  # Changed to 26 for A-Z
dataset_size = 100

camera_index = 0  # Change this if camera isn't found

cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    raise RuntimeError(f"Failed to open camera with index {camera_index}. Please check if the camera is connected and accessible.")
print(f"Using camera index: {camera_index}")
print(f"Collecting data for user: {USER_NAME}")

for j in range(number_of_letters):
    letter = LETTER_DICT[j]
    if not os.path.exists(os.path.join(DATA_DIR, letter)):
        os.makedirs(os.path.join(DATA_DIR, letter))

    print(f'Collecting data for user {USER_NAME}, letter {letter} ({j}/{number_of_letters-1})')

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'User: {USER_NAME} - Letter {letter} - Press "Q" to start!', 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.putText(frame, f'Capturing {counter}/{dataset_size}', 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        # New filename format: letter_USERNAME_number.jpg
        filename = f'{letter}_{USER_NAME}_{counter}.jpg'
        cv2.imwrite(os.path.join(DATA_DIR, letter, filename), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
