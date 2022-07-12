from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com")


name_input = driver.find_element(By.NAME, "fName")
name_input.send_keys("Felipe")

last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Coimbra")

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("felipe@email.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click( )
""" article_numbers = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER) """