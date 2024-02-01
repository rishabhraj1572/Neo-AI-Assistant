import cv2
import numpy
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands(
    model_complexity=1,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def hands_change(hand_coordinates, previous_hand_coordinates):
    if hand_coordinates:
        is_hand = True
    else:
        is_hand = False
    hand_state_change = False
    if hand_coordinates and not previous_hand_coordinates:
        hand_state_change = True
    if not hand_coordinates and previous_hand_coordinates:
        hand_state_change = True
    return is_hand, hand_state_change

def draw_hands_on_image(image, hand_coordinates, width, height):
    for position in hand_coordinates.landmark:
        x = int(position.x * width)
        y = int(position.y * height)
        cv2.circle(image, (x, y), 2, (0,255,0), 2, 2)
    return image

def process_coordinates(image, width, height):
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    hand_coordinates = []

    if results.multi_hand_landmarks:
        for mp_hand_coordinates in results.multi_hand_landmarks:
            hand_coordinates = mp_hand_coordinates

    return image, hand_coordinates