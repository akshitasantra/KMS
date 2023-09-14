import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import threading

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


def vote():
   try:
       driver = webdriver.Chrome()

       driver.get(
           "https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by"
           "-freddys")

       while len(driver.find_elements(By.CLASS_NAME, "show-more")) == 0:
           time.sleep(1)

       time.sleep(1)
       link = driver.find_element(By.CLASS_NAME, "show-more")
       link.click()

       while len(driver.find_elements(By.ID, "PDI_answer57332800")) == 0:
           time.sleep(1)

       answer_box = driver.find_element(By.ID, "PDI_answer57332800")
       answer_box.click()

       while len(driver.find_elements(By.ID, "pd-vote-button12735729")) == 0:
           time.sleep(1)

       vote_button = driver.find_element(By.ID, "pd-vote-button12735729")
       vote_button.click()

       time.sleep(2)

       if len(driver.find_elements(By.ID, "captcha_12735729")) > 0:
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
       print("Vote cast successfully")
   except:
       print("Vote unsuccessful")
       traceback.print_exc()


while True:
   t1 = threading.Thread(target=vote, args=())
   t2 = threading.Thread(target=vote, args=())
   t3 = threading.Thread(target=vote, args=())
   t4 = threading.Thread(target=vote, args=())
   t5 = threading.Thread(target=vote, args=())
   t6 = threading.Thread(target=vote, args=())
   t7 = threading.Thread(target=vote, args=())
   t8 = threading.Thread(target=vote, args=())
   t9 = threading.Thread(target=vote, args=())
   t10 = threading.Thread(target=vote, args=())
   t11 = threading.Thread(target=vote, args=())
   t12 = threading.Thread(target=vote, args=())
   t13 = threading.Thread(target=vote, args=())
   t14 = threading.Thread(target=vote, args=())
   t15 = threading.Thread(target=vote, args=())
   t16 = threading.Thread(target=vote, args=())

   t1.start()
   t2.start()
   t3.start()
   t4.start()
   t5.start()
   t6.start()
   t7.start()
   t8.start()
   t9.start()
   t10.start()
   t11.start()
   t12.start()
   t13.start()
   t14.start()
   t15.start()
   t16.start()

   # t1.join()
   # t2.join()
   # t3.join()
   # t4.join()
   # t5.join()
   # t6.join()
   # t7.join()
   # t8.join()
   # t9.join()
   # t10.join()
   # t11.join()
   # t12.join()
   # t13.join()
   # t14.join()
   # t15.join()
   t16.join()


