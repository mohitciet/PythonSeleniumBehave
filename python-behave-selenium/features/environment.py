from features.base.browser import Browser
from features.pages.home_page import HomePage
from features.pages.loginPage import LoginPage
from features.pages.search_results_page import SearchResultsPage
from features.base.selenium_driver import SeleniumDriver
from behave.model import *


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login  =  LoginPage()
    context.search_results_page = SearchResultsPage()
    context.selenium=SeleniumDriver()

def after_all(context):
    context.browser.close()

def after_step(context,step):
    if(step.status=="failed"):
        context.selenium.screenShot("Fail")

