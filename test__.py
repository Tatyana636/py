from seleniumwire import webdriver

driver = webdriver.Chrome("/home/evgenii/py/pyautogui/chromedriver")
# website = "https://psy.edu.ru/category"
website = "https://edu.i-spo.ru/"
driver.maximize_window()
driver.get(website)

email = driver.find_element_by_xpath("""//input[@autocomplete='off' and @class='form-common' and @id='email_inline_556' and @inputmode='email' and @maxlength='50' and @name='email' and @required='' and @type='email' and @value='']""")


button = driver.find_element_by_xpath("//button[@data-test]")

button.click()


# email = driver.find_element_by_xpath("""//input[@autocomplete='off' and @class='form-common' and @data-rq='^(([^а-я<>()[\]\\.,;:\s@"]+(\.[^а-я<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$' and @id='email_inline_556' and @inputmode='email' and @maxlength='50' and @name='email' and @required='' and @type='email' and @value='']""")
email.send_keys("smth")

from time import sleep

sleep(20)

driver.close()
driver.quit()