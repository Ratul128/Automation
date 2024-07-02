from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_url():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) #to access firefox
    driver.maximize_window() #to maximize the window

    driver.get("https://www.google.com/") #to get access website
    url=driver.current_url  #to get the browser url
    print(url)
    driver.close()

get_url()