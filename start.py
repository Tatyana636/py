from seleniumwire import webdriver
import pyautogui
from time import sleep
from bs4 import BeautifulSoup
from cookie import check_cookie
from conftest import setup_driver

website = "https://pentaschool.ru/program/dizajn-interera-intensiv-dlya-nachinayushchih?testBasic"

def start(link):
    driver = setup_driver
    if driver.current_url != link:
        driver.get(link)
        check_cookie(driver, website, {"name": "metric_off", "value": "1"})


input_FCs = driver.find_element_by_xpath("//input[@name='name'][1]")
input_tel = driver.find_element_by_xpath("//input[@name='phone'][1]")
input_email = driver.find_element_by_xpath("//input[@name='email'][1]")

input_FCs.send_keys('текст')

input_email.send_keys('tester_form@gaps.edu.ru')

btn = driver.find_element_by_xpath("//div[@class='quest-f-but']/button[1]")

_forms = driver.find_elements_by_xpath("//form[@data-test]")

__form = []

for f in _form:
    _form.
    #получить все xpath

form = Form(xpath="//form[@data-test='']", driver=driver)
form.Test()



data = {"tag": "form", "attrib": {a:b, c:d}} -> "//form[@a='b' and @c='d']"

start(website)