from behave import *
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from features.pages import loginPage
from features.environment import *
import unittest


@given(u'I navigate to the login page')
def step_impl(context):
    context.browser.navigateToUrl()

@when(u'I enter the username "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.login.login(username,password)



@then(u'I am able to login')
def step_impl(context):
   result=context.login.verifyLoginSuccessfull()
   assert result==True

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    pass
