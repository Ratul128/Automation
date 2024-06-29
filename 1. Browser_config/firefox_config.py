from selenium import webdriver

def firefox_launch():
    driver= webdriver.Firefox()

    driver.close()
firefox_launch()