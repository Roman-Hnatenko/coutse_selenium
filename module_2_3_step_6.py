import math
import time

from selenium import webdriver


def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )  

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element_by_class_name("btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_string = browser.find_element_by_id("input_value")
x_number = int( x_string.text )


answer = calc(x_number)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(answer)

send_button = browser.find_element_by_class_name("btn-primary")
send_button.click()


time.sleep(1)
