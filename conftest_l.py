import time
from selenium import webdriver
import pytest

@pytest.fixture()
def _driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/login")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()