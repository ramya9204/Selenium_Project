# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

