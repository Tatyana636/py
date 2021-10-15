#Считывание количества форм на странице
class readingNumberForms():

    def __init__(self, driver, link):
        self.driver = driver
        self.link = link


    def readingForms(driver, link):
        forms = self.driver.find_element_by_xpath("<form")

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
