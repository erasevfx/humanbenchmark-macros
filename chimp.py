import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui

print("Started")
print(pyautogui.position())

pyautogui.click(1275, 575)

chrome_options = Options()
chrome_options.debugger_address = "localhost:9222"

try:
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    print("Connected to Chrome session.")
except Exception as e:
    print(f"Error connecting to Chrome: {e}")
    exit()


def getNums():
    number_elements = driver.find_elements(By.CLASS_NAME, "css-19b5rdt")
    numbers = []
    for element in number_elements:
        number_text = int(element.text)
        numbers.append((number_text, element))
        
    numbers.sort(key=lambda x: x[0])

    for number, element in numbers:
        element.click()
    pyautogui.click(1275, 535)

for x in range(40):
    getNums()

driver.quit()
