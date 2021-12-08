from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


num1_in_text = browser.find_element_by_id("num1")
num2_in_text = browser.find_element_by_id("num2")

num1 = int(num1_in_text.text)
num2 = int(num2_in_text.text)

select = Select(browser.find_element_by_class_name("custom-select"))
select.select_by_value(str(num1 + num2))

send_button = browser.find_element_by_class_name("btn-default")
send_button.click()
sleep(10)
browser.quit()
