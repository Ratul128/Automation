from selenium import webdriver

def open_webpage_offline():
    driver= webdriver.Firefox()
    driver.get("file:///Users/nurulamin/Desktop/Python Learning/Your Store.htm")

    driver.close()

open_webpage_offline()