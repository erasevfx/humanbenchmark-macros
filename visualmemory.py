import time
import pyautogui
from PIL import Image
import numpy as np
import cv2
from PIL import ImageGrab

print("Started")
time.sleep(3)
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

    positions = []
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2
            positions.append((center_x, center_y))

    return positions

def click_squares(positions):
    for x, y in positions:
        pyautogui.click(region[0] + x, region[1] + y)
        print(f"Clicking square at ({x}, {y})")

pyautogui.click(1283, 535)

for x in range(100):
    screenshot = capture_screenshot()

    flashing_squares = find_flashing_squares("screenshot.png")

    if flashing_squares:
        print(f"Flashing squares detected at: {flashing_squares}")

        time.sleep(1.5)
        click_squares(flashing_squares)
    
    time.sleep(1)

print("Script finished.")
