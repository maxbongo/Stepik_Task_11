import os
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\yamko\\PycharmProjects\\pythonProject\\chromedriver\\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    num1 = int(x)
    z = str(math.log(abs(12 * math.sin(int(x)))))

    ans = browser.find_element_by_id('answer')
    ans.send_keys(z)

    button1 = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()