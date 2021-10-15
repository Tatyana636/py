# Проверка валидации
def hasItPassedValidation(driver, input):
        try:
            if(input=="input_FCs"):
                error = driver.find_element_by_xpath("//div[@class='still-quest_item'][1]//span[@class='err_message']]")
                if len(error.text)!=0:
                    return False                      #не прошло валидацию
                else:
                    return True   #прошло валидацию
            if(input=="input_tel"):
                error = driver.find_element_by_xpath("//div[@class='still-quest_item'][2]//span[@class='err_message']]")
                if  len(error.text)!=0:
                    return False                      #не прошло валидацию
                else:
                    return True
            if(input=="input_email"):
                error = driver.find_element_by_xpath("//div[@class='still-quest_item'][3]//span[@class='err_message']]")
                if  len(error.text)!=0:
                    return False                      #не прошло валидацию
                else:
                    return True
        except Exception as e:
            print(str(e))
            raise e