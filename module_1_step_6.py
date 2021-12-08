import math
from time import sleep

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

chest = browser.find_element_by_id("treasure")
x_value = chest.get_attribute("valuex")


first_test_result = calc(x_value)


first_test_input = browser.find_element_by_id("answer")
first_test_input.send_keys(first_test_result)


robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_checkbox.click()


robot_radiobutton = browser.find_element_by_id("robotsRule")
robot_radiobutton.click()

send_button = browser.find_element_by_class_name("btn-default")
send_button.click() 
sleep(10)
browser.quit()
