from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def set_browser_size():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(360,740)
    driver.get("https://www.google.com/")
    print(driver.get_window_size())
    driver.close()

set_browser_size()