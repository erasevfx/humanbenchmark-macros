import pyautogui
import time

time.sleep(3)

pyautogui.click(x=1000, y=500)

while (True):
    if pyautogui.pixelMatchesColor(1000, 500, (75, 219, 106)):
        pyautogui.click(x=1000, y=500)
        time.sleep(1)
        pyautogui.click(x=1000, y=500)