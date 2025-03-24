from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#3 Математическая функция от x

#1 Открыть страницу
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

#2 Считываем значение x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

#4 Скролим страницу вниз
browser.execute_script("window.scrollBy(0, 150);")

#5 Вводим ответ в поле
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
time.sleep(1)

#6 Выбираем checkbox I'm the robot
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

#7 Переключаем radiobutton Robots rule!
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()

#8 Submit
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(3)
#Чтобы успеть скопировать код

browser.quit()
