import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Set up WebDriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)

# Open the website
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)

#login to the website
driver.find_element("xpath",'//a[text()="Log in"]').click()
driver.find_element("id","Email").send_keys("ramya243@gmail.com")
driver.find_element("id","Password").send_keys("mango@123")
driver.find_element("xpath",'(//input[@type="submit"])[2]').click()

# search for product
driver.find_element("xpath","//input[@name='q']").send_keys("Book")
driver.implicitly_wait(2)
driver.find_element("xpath","//input[@type='submit']").click()

# Add product to cart
driver.find_element("xpath","//input[@value='Add to cart']").click()

# Go to cart
driver.find_element("xpath","(//span[@class='cart-label'])[1]").click()

#Click on Terms of service before checkout
driver.find_element("id","termsofservice").click()

#Click on checkout
driver.find_element("id","checkout").click()

#Fill Billing details
# listbox = driver.find_element("id","BillingNewAddress_CountryId")
# select_obj = Select(listbox)
# select_obj.select_by_visible_text("India")
# driver.find_element("id","BillingNewAddress_City").send_keys("Bangalore")
# driver.find_element("id","BillingNewAddress_Address1").send_keys("#17")
# driver.find_element("id","BillingNewAddress_ZipPostalCode").send_keys("560097")
# driver.find_element("id","BillingNewAddress_PhoneNumber").send_keys("7829801086")
time.sleep(2)
list_object = driver.find_element("id","billing-address-select")
sel_obj = Select(list_object)
val = sel_obj.select_by_index(0)


driver.find_element("xpath",'(//input[@title="Continue"])[1]').click()
# driver.find_element("class","button-1.new-address-next-step-button").click()
time.sleep(2)
# driver.find_element("xpath",'(//input[@title="Continue"])[1]').click()
# driver.find_element("xpath","(//input[@title='Continue'])[1]").click()

#shipping address
driver.find_element("xpath","(//input[@title='Continue'])[2]").click()

##Shipping method
driver.find_element("xpath","(//input[@value='Continue'])[3]").click()

#Payment method
driver.find_element("xpath","(//input[@value='Continue'])[4]").click()

#Payment Information
driver.find_element("xpath","(//input[@value='Continue'])[5]").click()

#Confirm order
driver.find_element("xpath",'//input[@value="Confirm"]').click()







