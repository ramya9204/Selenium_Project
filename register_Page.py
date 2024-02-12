import time
from selenium import webdriver
from framework_demowebpage_register.data import reading_objects
from framework_demowebpage_register.Library.sel_Wrapper import SeleniumWrapper

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()
# time.sleep(2)

register_objects = reading_objects.read_locators()

class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
        self.sel_Wrapper = SeleniumWrapper(driver)

    def enter_firstName(self):
        # driver.find_element(*register_objects["FirstName"]).send_keys("Ramya")
        self.sel_Wrapper.enter_text(register_objects["FirstName"],"Ramya")

    def enter_lastName(self):
        # driver.find_element(*register_objects["LastName"]).send_keys("K")
        self.sel_Wrapper.enter_text(register_objects["LastName"],"K")

    def enter_email(self):
        # driver.find_element(*register_objects["Email"]).send_keys("ramya243@gmail.com")
        self.sel_Wrapper.enter_text(register_objects["Email"],"ramya243@gmail.com")

    def enter_password(self):
        # driver.find_element(*register_objects["Password"]).send_keys("mango@123")
        self.sel_Wrapper.enter_text(register_objects["Password"],"mango@123")

    def enter_confirmpassword(self):
        # driver.find_element(*register_objects["ConfirmPassword"]).send_keys("mango@123")
        self.sel_Wrapper.enter_text(register_objects["ConfirmPassword"],"mango@123")

    def click_Submit(self):
        # driver.find_element(*register_objects["submit"]).click()
        self.sel_Wrapper.click_Element(register_objects["submit"])


# rp = RegisterPage(driver)
# rp.enter_firstName()
# rp.enter_lastName()
# rp.enter_email()
# rp.enter_password()
# rp.enter_confirmpassword()
# rp.click_Submit()