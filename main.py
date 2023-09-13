from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome()
while(True):
    driver.get("https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by"
              "-freddys")
    time.sleep(10)

    # = driver.find_element(By.ID, "PDI_answer57332800")


    #answer_text = "Tomball Cougars"
    #tomball_cougars = answer_box.find_element(By.XPATH, f".//label[contains(., '{answer_text}')]/preceding-sibling::span/input")



    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "show-more")))
    link.click()

    answer_box = driver.find_element(By.ID, "PDI_answer57332800")
    time.sleep(7)
    answer_box.click()

    vote_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pd-vote-button12735729")))
    time.sleep(7)
    vote_button.click()

    time.sleep(7)


    if(len(driver.find_elements(By.ID, "captcha_12735729")) > 0):
            answer_sheet = driver.find_element(By.ID, "captcha_12735729")
            numbers = answer_sheet.text.split('+')
            num1 = int(numbers[0].strip())
            numbers[1] = numbers[1].split("=")[0].strip()
            num2 = int(numbers[1].strip())
            result = num1 + num2
            answer_box = driver.find_element(By.ID, "answer_12735729")
            answer_box.send_keys(result)
            answer_box.send_keys(Keys.ENTER)

    time.sleep(7)




