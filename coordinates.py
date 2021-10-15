import csv

from requests.models import Response
from seleniumwire import webdriver
import pyautogui
from time import sleep
from bs4 import BeautifulSoup
import requests
import re

driver = webdriver.Chrome("/home/evgenii/py/pyautogui/chromedriver")
# website = "https://psy.edu.ru/category"
website = "https://edu.i-spo.ru/"
driver.maximize_window()
driver.get(website)

# Access requests via the `requests` attribute

# website = "https://hrmoscow.ru/category/kursy-dlya-rukovoditelej"

# phone = driver.find_element_by_xpath("(//input[@class='progr-form-elem'])[6]")
# phone.send_keys("81234567890")

# driver.maximize_window()
# driver.get(website)

# result = None
# for req in driver.requests:
#     if "phone=81234567890" in req.body.encode("utf-8"):
#         result = req
# result.response.status_code==200
# result.response.body 


def check_cookie(driver, url, cookie_dict):
    if driver.get_cookie(name=cookie_dict["name"]) is None:
        driver.add_cookie(cookie_dict=cookie_dict)

check_cookie(driver, website, {"name": "metric_off", "value": "1"})

# sleep(20)
arr=[]
r = requests.get(website)
soup = BeautifulSoup(r.content,"lxml")
blocks_cost = soup.select('form[data-test]')


from func4test import DataToXpath
from form import Form

for form in blocks_cost:
    xpath = DataToXpath({"tag": "form", "attrib": form.attrs})
    
    form = Form(xpath=xpath, driver=driver)
    form.Test()
    # print(form, "    ", )




# elem = soup.select("")
# input_FCs = driver.find_element_by_xpath("//input[@name='name'][1]")
# input_tel = driver.find_element_by_xpath("//input[@name='phone'][1]")
# input_email = driver.find_element_by_xpath("//input[@name='email'][1]")
# # for 
# # print(blocks_cost[3])

# # input_FCs.clear()
# # input_FCs.send_keys("aaaa")
# # v = pyautogui.locateOnScreen("mask.png")
# # print(v)
# # pyautogui.moveTo(v)


# location = input_FCs.location 
# size = input_FCs.size 
# driver.execute_script(f"window.scrollTo({location['x']}, {location['y']-850});")
# input_FCs.send_keys('текст')

# pyautogui.scroll(100, location['x'], location['y'])
# pyautogui.click(x=location['x']+1990, y=1000, clicks=1) 
# pyautogui.hotkey('текст')
# sleep(4)

# currentMouseX, currentMouseY = pyautogui.position()

# location = input_tel.location 
# pyautogui.click(x=location['x']+1990, y=989, clicks=1) 
# pyautogui.typewrite('81234567890')
# input_FCs.send_keys('tester_form@gaps.edu.ru'')

# pyautogui.hotkey('win', 'space')
# location = input_email.location 
# pyautogui.click(x=location['x']+1990, y=989, clicks=1) 
# pyautogui.typewrite('tester_form@gaps.edu.ru')
# input_email.send_keys('tester_form@gaps.edu.ru')

# print(currentMouseX, currentMouseY)
# btn = driver.find_element_by_xpath("//div[@class='quest-f-but']/button[1]")
# btn.click()
# sleep(4)
# for request in driver.requests:
#     if request.response:
        # print(
        #     request.url,
        #     request.response.status_code,
        #     request.response.headers['Content-Type'],
        #     # requests.response.json()
        #    )
        # if((request.response.status_code==200 or  request.response.status_code==404 or request.response.status_code==500) and request.response.headers['Content-Type']=='text/html; charset=UTF-8'):
            # if request.url == 'https://psy.edu.ru/ajax/order_processing':
            # try:
            #     if(re.search(r'81234567890', request.body.decode("utf-8")).group(0)=='81234567890'):
            #         print(
            #             request.url,
            #             request.response.status_code,
            #             request.response.headers['Content-Type'],
            #             request.response.body.decode("utf-8"),
                            # request.body.decode("url")
            #     )
            # except Exception as e:
            #     e
# sleep(4)
# # pyautogui.mouseUp(location['x']+1920, 850, button='left')
# # sleep(4)

# # input_FCs.click()


# print(size)


# _forms = driver.find_elements_by_xpath("//form[@data-test]")

# __form = []

# for f in _form:
#     _form.
#     #получить все xpath

# form = Form(xpath="//form[@data-test='']", driver=driver)
# form.Test()



# data = {"tag": "form", "attrib": {a:b, c:d}} -> "//form[@a='b' and @c='d']"

driver.close()
driver.quit()