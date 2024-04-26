from selenium import webdriver
from selenium.webdriver.chrome import service as ChromeService
from selenium.webdriver.common import By
from webdriver_manager import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
