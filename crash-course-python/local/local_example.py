# Selenium 3.14+ doesn't enable certificate checking
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium import webdriver

os_version = 'mac64'
driver_version = 'chromedriver80'
driver = webdriver.Chrome('./webdrivers/' + os_version + '/' + driver_version + '/chromedriver')
driver.get("https://www.saucedemo.com")

driver.find_element_by_id('user-name').send_keys('standard_user')
driver.find_element_by_id('password').send_keys('secret_sauce')
driver.find_element_by_css_selector("[type='submit']").click()

actual_result = "passed" if driver.current_url == "https://www.saucedemo.com/inventory.html" else "failed"
print('The test ' + actual_result)
driver.quit()