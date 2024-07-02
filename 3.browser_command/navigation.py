import time

from selenium import webdriver
def navigate():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    driver.get("https://google.com/")
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.refresh()
    driver.close()

navigate()