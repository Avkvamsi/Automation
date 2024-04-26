# importing the webdriver from selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/")

driver.quit()
