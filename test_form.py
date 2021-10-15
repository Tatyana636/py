import pytest
from selenium import webdriver
import pyautogui
import validation_check

website = "https://pentaschool.ru"


# Ожидание загрузки страницы
def wait_for_element_to_load(driver):
    try:
        return WebDriverWait(driver, 30).until(lambda driver : driver.find_element_by_xpath("html"))
    finally:
        pass


def pytest_generate_tests(metafunc):
    try:
        links = []
        with open("list.txt", "r", encoding='utf-8') as file:
            for url in file:
                links.append(url[:-1]) 
    except FileExistsError as e:
        raise e

    metafunc.parametrize("link", links)

def check_cookie(driver, url, cookie_dict):
    if driver.get_cookie(name=cookie_dict["name"]) is None:
        driver.get(url=url[0:url.find(".ru") + 3])
        driver.add_cookie(cookie_dict=cookie_dict)


def readingForms(driver, link):
    forms = driver.find_element_by_xpath("<form")
    for vl in forms:
        

    input_FCs = driver.find_element_by_xpath("//input[@class='gtm__question_name gtm__question_input']")
    input_tel = driver.find_element_by_xpath("//input[@name='phone']")
    input_email = driver.find_element_by_xpath("//input[@class='gtm__question_email gtm__question_input']")
    btn = driver.find_element_by_xpath("//button[@class='btn btn-pink gtm__question_submit']")
    form_name = 
    
    link= link

  coordinates_FCs, location = readingCoordinates(input_FCs)
    coordinates_tel = readingCoordinates(input_tel)
    coordinates_email = readingCoordinates(input_emai

    driver.execute_script(f"window.scrollTo({location['x']}, {location['y']-850});")

        result_FCs = validation_check.hasItPassedValidation(driver, "input_FCs")
    result_tel = validation_check.hasItPassedValidation(driver, "input_tel")
    result_email = validation_check.hasItPassedValidation(driver, "input_email")
   btn.click()


#считывание координат
def readingCoordinates(input):
  return input.location
  

# Заполнение полей формы
def fillingFormFields(driver, location):   
    pyautogui.click(x=location['x']+1990, y=989, clicks=1) 
    pyautogui.typewrite('1234567890')
  

def test_A(setup_driver, link):
    driver = setup_driver
    check_cookie(driver, website, {"name": "metric_off", "value": "1"})
    if driver.current_url != link:
        driver.get(link)
    
    wait_for_element_to_load(driver)
    
    result = readingNumberForms(driver, link)
    # input_FCs.clear()
    # input_FCs.send_keys(case)

    # input_email.send_keys("")
    assert result["res_FCs"]==result["res_tel"]==result["res_email"]==False, f"Не прошли валидацию формы {result['form']}, ссылка {result['res_link']}"
    
