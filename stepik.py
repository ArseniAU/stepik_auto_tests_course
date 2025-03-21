from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

element_locator = (By.ID, "price")
wait = WebDriverWait(browser, 12)

#условие ожидания - появление текста
wait.until(EC.text_to_be_present_in_element(element_locator, "$100"))
button = browser.find_element(By.ID, "book")
button.click()
time.sleep(1)

#4 Скролим страницу вниз
browser.execute_script("window.scrollBy(0, 300);")

#считываем x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

#5 Вводим ответ в поле
input = browser.find_element(By.ID, "answer")
input.send_keys(y)

#вторая кнопка
button_second = browser.find_element(By.ID, "solve")
button_second.click()
time.sleep(1)

time.sleep(5)
browser.quit()