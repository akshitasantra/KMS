# Idk if this works Akshita if your reading this HELP

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.vype.com/Texas/Houston/vype-hou-public-school-cheer-team-of-the-year-fan-poll-presented-by-freddys")
assert "Public School Cheer Team of the Year" in driver.title

driver.find_element_by_link_text("Keep reading...").click()

option_xpath = '//*[@id="pds-answer12735729"]/div[23]/div/label/span'
selected_option = driver.find_element_by_xpath(option_xpath).click()

submit_button_xpath = '//*[@id="pd-vote-button12735729"]'
submit_button = driver.find_element_by_xpath(submit_button_xpath).click()

