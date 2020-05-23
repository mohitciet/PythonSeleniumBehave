from selenium import webdriver

class Browser(object):
    baseURL = "https://letskodeit.teachable.com/"
    browser = "chrome"
    if browser == "iexplorer":
        # Set ie driver
        driver = webdriver.Ie()
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="D:/PythonSeleniumFW/configfiles/geckodriver.exe")
    elif browser == "chrome":
        # Set chrome driver
        # chromedriver = "/Users/atomar/Documents/workspace_personal/selenium/chromedriver"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)
        # driver.set_window_size(1440, 900)
        driver = webdriver.Chrome(executable_path="D:/PythonSeleniumFW/configfiles/chromedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="D:/PythonSeleniumFW/configfiles/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def navigateToUrl(context):
        # Loading browser with App URL
        context.driver.get(context.baseURL)
