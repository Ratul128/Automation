from selenium import webdriver

def chrome_launch():
    driver= webdriver.Chrome()

    driver.close()
chrome_launch()