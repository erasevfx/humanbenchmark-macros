import sys
import cv2
import numpy as np
import mss
from pynput.mouse import Button, Controller

mouse = Controller()

CAPTURE_REGION = {
    "left": 540,
    "top": 152,
    "width": 1134,
    "height": 615,
}

CIRCLE_PARAMS = {
    "dp": 1.2,
    "minDist": 30,
    "param1": 40,
    "param2": 25,
    "minRadius": 25,
    "maxRadius": 50,
}

DOWNSCALE_FACTOR = 0.75

def process_frame(frame):
    """Convert frame to grayscale, downscale, and apply Gaussian blur."""
    frame = cv2.resize(frame, (0, 0), fx=DOWNSCALE_FACTOR, fy=DOWNSCALE_FACTOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(gray, (5, 5), 0), frame

def detect_circles(gray_frame):
    """Detect circles in the grayscale frame."""
    return cv2.HoughCircles(
        gray_frame,
        cv2.HOUGH_GRADIENT,
        dp=CIRCLE_PARAMS["dp"],
        minDist=CIRCLE_PARAMS["minDist"] * DOWNSCALE_FACTOR,
        param1=CIRCLE_PARAMS["param1"],
        param2=CIRCLE_PARAMS["param2"],
        minRadius=int(CIRCLE_PARAMS["minRadius"] * DOWNSCALE_FACTOR),
        maxRadius=int(CIRCLE_PARAMS["maxRadius"] * DOWNSCALE_FACTOR),
    )

def main():
    with mss.mss() as stc:
        while True:
            scr = stc.grab(CAPTURE_REGION)
            frame = np.array(scr)

            gray, downscaled_frame = process_frame(frame)
            circles = detect_circles(gray)

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    x = int(x / DOWNSCALE_FACTOR)
                    y = int(y / DOWNSCALE_FACTOR)
                    r = int(r / DOWNSCALE_FACTOR)

                    cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                    
                    mouse.position = (x + CAPTURE_REGION["left"], y + CAPTURE_REGION["top"])
                    mouse.click(Button.left, 1)

if __name__ == "__main__":
    main()
