import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print("Started")
wordList = []
time.sleep(1)
chrome_options = Options()
chrome_options.debugger_address = "localhost:9222"

try:
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    print("Connected to Chrome session.")
except Exception as e:
    print(f"Error connecting to Chrome: {e}")
    exit()

def getWord():
    try:
        newWord = driver.find_element(By.CLASS_NAME, "word").text
        
        if (len(wordList) == 0):
            wordList.append(newWord)
            clickButton(True)
        else:
            if (newWord in wordList):
                clickButton(False)
            else:
                wordList.append(newWord)
                clickButton(True)
    except Exception as e:
        print(f"Error extracting letters: {e}")
        driver.quit()
        exit()

def clickButton(isNew):
    if (isNew):
        pyautogui.click(1328, 480)
    else:
        pyautogui.click(1205, 485)

for x in range(1000):
    getWord()

print(wordList)
driver.quit()