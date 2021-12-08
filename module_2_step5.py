import math
import os
from time import sleep

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name_field = browser.find_element_by_css_selector("[name='firstname']")
lastname_field = browser.find_element_by_css_selector("[name='lastname']")
email_field = browser.find_element_by_css_selector("[name='email']")
file_button = browser.find_element_by_css_selector("[type='file']")
send_button = browser.find_element_by_css_selector(".btn-primary")


name_field.send_keys("H")
lastname_field.send_keys("F")
email_field.send_keys("y")

current_dir = os.path.abspath(os.path.dirname(__file__))


file_path = os.path.join(current_dir, "test_file.txt")


file_button.send_keys(file_path)
send_button.click()
sleep(10)
browser.quit()
