from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    # input3 = browser.find_element_by_name('email')
    # input3.send_keys("bla")

    # Отправляем заполненную форму
    button = browser.find_element_by_id("book")
    button.click()

    # old_window, new_window = browser.window_handles
    # browser.switch_to.window(new_window)

    input1 = browser.find_element_by_id('input_value')
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(f'{calc(input1.text)}')

    button = browser.find_element_by_id("solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
