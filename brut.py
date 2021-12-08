
import math
import random
from itertools import combinations
from time import sleep
from typing import Tuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
LOGIN = 'h.natenkoroman@gmail.com'
PASSWORD = ',fh,fhjcf9'
LINK_ON_TEST = 'https://stepik.org/lesson/236918/step/7?unit=209305'

WRONG_WARIANTS = ()

answers = []

def set_global_data() -> None:
    global answers
    sleep(10)
    checkboxs = browser.find_elements_by_css_selector('.s-checkbox')
    for element in checkboxs:
        answers.append(element.text)
    
    
def press_button(selector: str, sleep_time: float = 1.0 ) -> None:
    button = browser.find_element_by_css_selector(selector)
    button.click()
    sleep(sleep_time)


browser.get("https://stepik.org/lesson/138920/step/13?unit=196194")
def log_in() -> None:
    sleep(5)
    press_button('a.navbar__auth')
    name_input = browser.find_element_by_css_selector('[name="login"]')
    name_input.send_keys(LOGIN)
    p_input = browser.find_element_by_css_selector('[name="password"]')
    p_input.send_keys(PASSWORD)
    press_button('button.sign-form__btn')

def choose_variants(combination: Tuple[int]) -> None:
    print(combination)
    for index in combination:
        text: str = answers[index]
        text = text.replace('\"', '')
        checkbox = browser.find_element_by_xpath(f'//span[contains (text(), "{text.strip()}" ) ]')
        checkbox.click()
    sleep(0.05)


def iterate_combinations():
    exclusion_indexes = set()
    for elem in WRONG_WARIANTS:
        if elem in answers:
            exclusion_indexes.add(answers.index(elem))
            
    elements = browser.find_elements_by_css_selector('.s-checkbox__border') or browser.find_elements_by_css_selector('.s-checkbox')
    elements_count = len(elements)
    for cur_len in range(1, elements_count + 1):
        for combitation in  combinations(range(elements_count), cur_len):
            if set(combitation) & exclusion_indexes:
                continue
            yield combitation

def try_reset() -> None:
    button_reset = browser.find_element_by_css_selector('button.again-btn')
    button_reset.click()
    
def create_answer(combination): 
    choose_variants(combination)
    press_button('button.submit-submission')
    if not browser.find_elements_by_css_selector('.attempt__wrapper_next-link'):
        try_reset()
        sleep(1)
    else:
        for index in combination:
            print(answers[index])
        sleep(1000)
        
if __name__ == "__main__":
    log_in()
    browser.get(LINK_ON_TEST)
    set_global_data()
    for combination in iterate_combinations():
        while True:
            try:
                print(combination)
                create_answer(combination)
                break
            except Exception as e:
                sleep(0.1)
                try:
                    try_reset()
                except Exception:
                    pass
                print('Connection error')
                
browser.quit()
