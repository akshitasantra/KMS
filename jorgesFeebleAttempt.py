# Idk if this works Akshita if your reading this HELP

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by-freddys")
assert "Public School Cheer Team of the Year" in driver.title

element_path = '/html/body/div[4]/div/div[5]/div/div/div[1]/div/div[1]/div/article/div/div/div[3]/div[3]/div/div[4]/span[1]'

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_path)))
element.click()

for i in range (5):
    time.sleep(4)
    option_xpath = '//*[@id="pds-answer12735729"]/div[23]/div/label/span'
    driver.find_element(By.XPATH,option_xpath).click()

    time.sleep(1)

    submit_button_xpath = '//*[@id="pd-vote-button12735729"]'
    driver.find_element(By.XPATH,submit_button_xpath).click()

    time.sleep(1)

    captcha_id = "h-captcha"
    captcha = driver.find_element(By.CLASS_NAME, captcha_id)
    captcha_text = captcha.text

    time.sleep(1)

    numbers = captcha_text.split('+')

    num1 = int(numbers[0].strip())
    num2 = int(numbers[1].strip())

    result = num1 + num2

    vote_button_xpath = '//*[@id="pd-vote-button12735729"]'
    driver.find_element(By.XPATH,vote_button_xpath).click()

    time.sleep(1)

    submit_field_id = "answer_12735729"
    submit_field = driver.find_element(By.ID, submit_field_id)
    submit_field.send_keys(result)

    time.sleep(1)

    driver.find_element(By.ID,"pd-vote-button12735729").click()
    driver.find_element(By.XPATH,'//*[@id="PDI_container12735729"]/div/div/div/div/div[5]/div/span[1]/a').click()

    time.sleep(1)
    print("Success!"+i)




