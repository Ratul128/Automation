from selenium import webdriver

def open_webpage_online():
    driver= webdriver.Firefox()
    driver.get("https://www.google.com/")

    driver.close()

open_webpage_online()