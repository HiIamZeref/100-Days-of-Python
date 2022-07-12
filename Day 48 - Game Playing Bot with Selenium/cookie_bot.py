from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

break_time = time.time() + 1
final_time = time.time() + 5*60

chrome_driver_path = 'D:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_click = driver.find_element(By.ID, "cookie")
game = True




while game:
    if final_time < time.time():
        game = False
        cookies_per_second = driver.find_element(By.ID, "cps")
        print(cookies_per_second.text)
    elif break_time < time.time():
        break_time = time.time() + 1

        cookie_count = driver.find_element(By.ID, "money").text

        cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
        cursor_money = cursor.text.split("-")[1]

        grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        grandma_money = grandma.text.split("-")[1]
        
        factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        factory_money = factory.text.split("-")[1]
        
        

        if float(cookie_count) > float(factory_money):
            factory.click()
        elif float(cookie_count) > float(grandma_money):
            grandma.click()
        elif float(cookie_count) > float(cursor_money):
            cursor.click()
        
    
    cookie_click.click()



    