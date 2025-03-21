import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_file.txt"

file_path = os.path.join(current_dir, file_name)

first_name = browser.find_element(By.TAG_NAME, "input")
first_name.send_keys("Alexander")

last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys("TheGreat")

email_email = browser.find_element(By.XPATH, "//form//input[3]")
email_email.send_keys("randomail@pochta.ru")

time.sleep(1)

element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

time.sleep(1)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(3)

browser.quit()

