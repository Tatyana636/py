
def check_cookie(driver, url, cookie_dict):
    if driver.get_cookie(name=cookie_dict["name"]) is None:

        driver.add_cookie(cookie_dict=cookie_dict)