from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome()
driver.get("https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by"
          "-freddys")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Read More']"))
    )
    element.click()
except:
    print("didnt work")

