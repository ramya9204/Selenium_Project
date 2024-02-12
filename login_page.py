# from selenium import webdriver
# import time
#
# from framework_demowebshop.data import reading_objects
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()
# time.sleep(2)
#
# login_objects = reading_objects.read_locators()
#
# class LoginPage:
#     def enter_email(self):
#         driver.find_element(*login_objects["Email"]).send_keys("ramya243@gmail.com")
#     def enter_password(self):
#         driver.find_element(*login_objects["Password"]).send_keys("mango@123")
#     def click_login(self):
#         driver.find_element(*login_objects["login_btn"]).click()
#
# lp = LoginPage()
# lp.enter_email()
# lp.enter_password()
# lp.click_login()


from selenium import webdriver

from framework_demowebshop.data import reading_objects
from framework_demowebshop.Library.sel_wrapper import SeleniumWrapper

# import reading_objects
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()

login_objects = reading_objects.read_locators()

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.sel_wrapper = SeleniumWrapper(driver)

    def enter_email(self):
        self.sel_wrapper.enter_text(login_objects["Email"], "ramya243@gmail.com")

        # driver.find_element(*login_objects["Email"]).send_keys("ramya243@gmail.com")
    def enter_password(self):
        # driver.find_element(*login_objects["Password"]).send_keys("mango@123")
        self.sel_wrapper.enter_text(login_objects["Password"],"mango@123")

    def click_login(self):
        # driver.find_element(*login_objects["login_btn"]).click()
        self.sel_wrapper.click_element(login_objects["login_btn"])
# lp = LoginPage(driver)
# lp.enter_email()
# lp.enter_password()
# lp.click_login()

