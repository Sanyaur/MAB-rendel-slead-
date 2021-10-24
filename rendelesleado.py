from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
# import pyautogui as pg

from time import sleep
from datetime import datetime

PATH = 'c:/Program Files (x86)/geckodriver.exe'
driver = webdriver.Firefox(executable_path=PATH)


driver.get('https://www2.avon.hu/hu-home/orders/product-entry')
driver.maximize_window() #window set to max

def login_field():
    # locating elements
    username = driver.find_element_by_id('sellerUserId')
    password = driver.find_element_by_id('sellerEmailPassword')
    login_button = driver.find_element_by_css_selector('button.lg-btn')
        
    # interacting w/ elements
    username.send_keys('6290011')
    password.send_keys('ezEgyJelszó!01' + Keys.ENTER)
    login_button.click()

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sellerEmailPassword")))
    print('login passed')
    login_field()
except:
    print('login failed')

def ln_input_field(num):
    ln_input_field = driver.find_element_by_css_selector(f'.shpByProdNum > tab-entry-core:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child({num}) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
    return ln_input_field
def county_box(num):
    ln_input_field = driver.find_element_by_css_selector(f'.shpByProdNum > tab-entry-core:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child({num}) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)')
    return ln_input_field

def LN_input_page():
    try:
        popup_button = '.dnt-btn > button:nth-child(1)'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, popup_button)))
        product_popup_X = driver.find_element_by_css_selector(popup_button)
        product_popup_X.click()
        print('popup closed')
    except:
        print('no popup')
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.shpByProdNum > tab-entry-core:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')))
        print('input fields ready')
    except:
        print('input fields failed')

    order_list = [
                63586, 1 ,63990, 1, 98103,1, 18531, 1, 46094
                    ]
    termeklista = order_list[::2]
    product_count = order_list[1::2]

    ln_input_field_child = 1
    for line_number in range(len(termeklista)):
        ln_input_field(ln_input_field_child).send_keys(str(termeklista[line_number]))
        county_box(ln_input_field_child).send_keys(str(product_count[line_number]))
        ln_input_field_child +=1
        sleep(0.7)

    termek_mentese_button = driver.find_element_by_css_selector('.shpByProdNum > tab-entry-core:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')
    termek_mentese_button.click()

    tovabb_button = driver.find_element_by_id('btnCont')
    tovabb_button.click()
LN_input_page()

quit()

def next_step_click(selector):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    driver.find_element_by_css_selector(selector).click()

next_step_click('.nxt-stp')
next_step_click('.nxt-stp')
next_step_click('button.sim-button:nth-child(2)')
sleep(0.5)
next_step_click('#ctn-ckout')