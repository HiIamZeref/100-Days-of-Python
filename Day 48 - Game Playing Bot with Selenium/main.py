from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver_path = 'D:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver_path)

upcoming_events = {}

driver.get("https://www.python.org")
event_dates = driver.find_elements(By.CSS_SELECTOR, "div.event-widget ul li time")
event_names = driver.find_elements(By.CSS_SELECTOR, "div.event-widget ul li a")



for index in range(0,5):
    upcoming_events[index] = {
        "time": event_dates[index].text,
        "name": event_names[index].text
    }

pprint(upcoming_events)


driver.quit()