import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )  

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)


browser = webdriver.Chrome(options=opt)
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()

x_string = browser.find_element_by_id("input_value")
x_number = int( x_string.text )

answer = calc(x_number)


input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(answer)


send_button = browser.find_element_by_id("solve")
send_button.click()
time.sleep(10)
browser.quit()
