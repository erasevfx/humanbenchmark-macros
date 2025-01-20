import pyautogui
import time
from PIL import Image
import numpy as np
import cv2
from PIL import ImageGrab

region = (1028, 231, 1590, 632)
def capture_screenshot():
    screenshot = ImageGrab.grab(bbox=region)
    screenshot.save("screenshot.png")
    return screenshot

def find_flashing_squares(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 50:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2
            return (center_x, center_y)

def perform_sequence(sequence):
    for tile in sequence:
        print(tile)
        pyautogui.click(tile[0], tile[1])


def get_sequence(x):
    sequence = []
    for y in range(x+1):
        time.sleep(0.45)
        screenshot = capture_screenshot()

        flashing_squares = find_flashing_squares("screenshot.png")
        if flashing_squares:
            sequence.append((flashing_squares[0] + 1028, flashing_squares[1] + 231))
    
    return sequence
        

pyautogui.click(1283, 535)


time.sleep(0.5)
for x in range(50):
        print(f"Round {x + 1} - Observing sequence...")
        sequence = get_sequence(x + 1)

        print("Sequence captured:", sequence)

        time.sleep(1)
        print("Replaying sequence...")
        perform_sequence(sequence)
        time.sleep(0.8)