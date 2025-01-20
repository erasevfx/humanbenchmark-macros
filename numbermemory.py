import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print("Started")
wordList = []

chrome_options = Options()
chrome_options.debugger_address = "localhost:9222"

try:
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    print("Connected to Chrome session.")
except Exception as e:
    print(f"Error connecting to Chrome: {e}")
    exit()

pyautogui.click(1275, 560)

for x in range(100):
    num = driver.find_element(By.CLASS_NAME, "big-number").text
    if (x < 5):
        time.sleep(1)
    time.sleep(1+x)
    pyautogui.click(1268, 411)
    pyautogui.typewrite(num)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

driver.quit()