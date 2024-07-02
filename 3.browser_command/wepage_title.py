from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_title():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) #to access firefox
    driver.maximize_window() #to maximize the window

    driver.get("https://www.google.com/") #to get access website
    title=driver.title  #to get the browser title
    print(title)
    driver.close()

get_title()