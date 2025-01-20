import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print("Started")

chrome_options = Options()
chrome_options.debugger_address = "localhost:9222"

try:
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    print("Connected to Chrome session.")
except Exception as e:
    print(f"Error connecting to Chrome: {e}")
    exit()

try:
    parent_element = driver.find_element(By.CSS_SELECTOR, ".letters.notranslate")
    print("Found parent element.")
except Exception as e:
    print(f"Error locating parent element: {e}")
    driver.quit()
    exit()

try:
    letter_elements = parent_element.find_elements(By.CSS_SELECTOR, "span.incomplete")
    letters = ""

    for letter_element in letter_elements:
        letter_text = letter_element.text
        if not letter_text:
            letters += " "
        else:
            letters += letter_text

    print("Extracted Letters:", repr(letters))
except Exception as e:
    print(f"Error extracting letters: {e}")
    driver.quit()
    exit()

driver.quit()

try:
    print("Typing letters...")
    pyautogui.typewrite(letters, interval=0.001)
    print("Done typing.")
except Exception as e:
    print(f"Error in typing with pyautogui: {e}")
