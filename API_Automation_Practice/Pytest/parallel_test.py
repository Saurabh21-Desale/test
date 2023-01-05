from selenium import webdriver

# to run parallel test we need to install pytest-xdist
# to run parallel test case py.test package name/file name.py -n 5
#
# 5 = 5 browsers run at a time

driver =webdriver.Edge(executable_path="C:\\Users\\saurabhd\\eclipse-workspace\\Selenium\\edgedriver_win64\\msedgedriver.exe")

# def teardown_module(module):
#     driver.quit()

def test_google():
    driver.get("https://www.google.co.in")
    assert driver.title=="Google"
    driver.quit()

def test_gmail():
    driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp")
    assert driver.title=="Create your Google Account"
    driver.quit()

def test_fb():
    driver.get("https://www.facebook.com/")
    assert driver.title=="Facebook – log in or sign up"
    driver.quit()

def test_insta():
    driver.get("https://www.instagram.com/")
    assert driver.title=="Instagram"
    driver.quit()
