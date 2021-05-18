from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome(executable_path="/Users/alvin_chun/Desktop/Python_Behave/Drivers/chromedriver")
    context.driver = webdriver.Chrome()

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True

@then('close browser')
def step_impl(context):
    context.driver.close()

