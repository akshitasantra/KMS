from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import threading

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


def vote():

    driver = webdriver.Chrome()

    driver.get(
        "https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by"
        "-freddys")


    time.sleep(2)

    while len(driver.find_elements(By.CLASS_NAME, "show-more")) == 0:
        time.sleep(2)

    link = driver.find_element(By.CLASS_NAME, "show-more")
    link.click()

    while len(driver.find_elements(By.ID, "PDI_answer57332800")) == 0:
        time.sleep(2)

    answer_box = driver.find_element(By.ID, "PDI_answer57332800")
    answer_box.click()

    while len(driver.find_elements(By.ID, "pd-vote-button12735729")) == 0:
        time.sleep(2)

    vote_button = driver.find_element(By.ID, "pd-vote-button12735729")
    vote_button.click()

    time.sleep(2)

    if len(driver.find_elements(By.ID, "captcha_12735729")) != 0:
        print("working")
        answer_sheet = driver.find_element(By.ID, "captcha_12735729")
        numbers = answer_sheet.text.split('+')
        num1 = int(numbers[0].strip())
        numbers[1] = numbers[1].split("=")[0].strip()
        num2 = int(numbers[1].strip())
        result = num1 + num2
        answer_box = driver.find_element(By.ID, "answer_12735729")
        answer_box.send_keys(result)
        time.sleep(1)
        answer_box.send_keys(Keys.ENTER)
        time.sleep(1)

    time.sleep(2)

while(True):
    t1 = threading.Thread(target=vote, args=())
    t1.start()
    t1.join()
