from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import features.utilities.custom_logger as cl
import logging
import os
import allure
from allure_commons.types import AttachmentType
from features.base.browser import Browser





class SeleniumDriver(Browser):
    log = cl.customLogger(logging.DEBUG)

    # def __init__(self,driver):
    #     super().__init__( driver)
    #     self.driver=driver


    def getByType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType == "id" :
            return By.ID
        elif locatorType == "name" :
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else :
            self.log.info("Invalid Locator Type =" + locatorType)

    def getElement(self, locator,locatorType):
        element=None
        try:
            locatorType = locatorType.lower()
            byType=self.getByType(locatorType)
            self.waitForElement(locator,byType)
            element= self.driver.find_element(byType, locator)
            self.log.info("Locator found Successfully with Locator Type="+byType+" and locator="+locator)
            self.log.info("***************************************************")
        except:
            self.log.error("Unable to Find with Locator Type="+locatorType+" and locator="+locator)
        return element

    def clickElement(self, locator,locatorType):
        element=None
        try:
            ##WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorType, locator)))
            element=self.getElement(locator,locatorType)
            self.highlight(element)
            element.click()
            self.log.info("Clicked on Element with Locator Type="+locatorType+" and locator="+locator)
            self.log.info("***************************************************")
        except:
            self.log.error("Cannot Click on Element with Locator Type="+locatorType+" and locator="+locator)

    def sendKeys(self, data,locator, locatorType):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            self.highlight(element)
            element.send_keys(data)
            self.log.info("Entered Data on Element with Locator Type=" + locatorType + " and locator=" + locator)
            self.log.info("***************************************************")
        except:
            self.log.error("Cannot Enter Data on Element with Locator Type=" + locatorType + " and locator=" + locator)

    def highlight(self,element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 4px solid red;")
        time.sleep(.2)
        apply_style(original_style)

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=1):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            #print_stack()
        return element

    def isElementPresent(self, locator,locatorType):
        element=None
        try:
            element=self.getElement(locator,locatorType)
            if element is not None:
                self.highlight(element)
                self.log.info("Element is present on Page with Locator Type="+locatorType+" and locator="+locator)
                self.log.info("***************************************************")
                return True
            else:
                self.log.error(
                    "Element is not present on Page with Locator Type=" + locatorType + " and locator=" + locator)
                return False

        except:
            self.log.error("Element not found on Page with Locator Type="+locatorType+" and locator="+locator)


    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
            allure.attach(self.driver.get_screenshot_as_png(),name='screenshot',attachment_type=AttachmentType.PNG)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            #print_stack()








