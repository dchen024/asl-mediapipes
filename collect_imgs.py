import os
import cv2

# Create a dictionary mapping numbers to letters (0-25 to A-Z)
LETTER_DICT = {i: chr(65 + i) for i in range(26)}  # 65 is ASCII for 'A'

# User configuration
USER_NAME = "daniel"  # Change this to your name
# Create a dictionary mapping numbers to letters (0-25 to A-Z)
LETTER_DICT = {i: chr(65 + i) for i in range(26)}  # 65 is ASCII for 'A'

# User configuration
USER_NAME = "daniel"  # Change this to your name
DATA_DIR = './data'
USER_DIR = os.path.join(DATA_DIR, USER_NAME)  # Create user-specific directory

# Create main data directory and user directory
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(USER_DIR):
    os.makedirs(USER_DIR)

number_of_letters = 2
dataset_size = 100

camera_index = 0

cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    raise RuntimeError(f"Failed to open camera with index {camera_index}. Please check if the camera is connected and accessible.")
print(f"Using camera index: {camera_index}")
print(f"Collecting data for user: {USER_NAME}")
print(f"Collecting data for user: {USER_NAME}")

for j in range(number_of_letters):
    letter = LETTER_DICT[j]
    letter_dir = os.path.join(USER_DIR, letter)
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)

    print(f'Collecting data for user {USER_NAME}, letter {letter} ({j + 1}/{number_of_letters})')

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'User: {USER_NAME} - Letter {letter} - Press "Q" to start!', 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3,
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
        cv2.putText(frame, f'Capturing {counter}/{dataset_size}', 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        filename = f'{USER_NAME}_{letter}_{counter}.jpg'
        cv2.imwrite(os.path.join(letter_dir, filename), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
