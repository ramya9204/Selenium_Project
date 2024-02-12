import time
from selenium import webdriver
import pytest

@pytest.fixture()
def _driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    yield driver
    # driver.close()



