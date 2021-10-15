import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--invisible", action='store_true', help="Run on virtual display")
    parser.addoption("--adaptive", action='store_true', help="Run as mobile user agent")
    parser.addoption("--fn", type=str, help="Path of file")
    parser.addoption("--site", type=str, help="Url of site")
    parser.addoption("--parse", action='store_true', help="Parse site on urls")


@pytest.fixture(scope="session")
def setup_driver(request):
    try:
        chrome_options = Options()
        if request.config.getoption("--invisible"):
            display = Display(visible=0, size=(1920, 1080))
            display.start()
        if request.config.getoption("--adaptive"):
            chrome_options.add_argument(
                '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        chrome_options.add_argument("--window-size=1920,1080")
        Driver = webdriver.Chrome("/home/evgenii/py/test_form/chromedriver", desired_capabilities=d, options=chrome_options)
    except Exception as e:
        raise e
    yield Driver
    try:
        Driver.close()
        Driver.quit()
        if request.config.getoption("--invisible"):
            display.stop()
    except Exception as e:
        raise e
