from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = 'D:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver_path)

MY_EMAIL =  "##########"
PASSWORD = "#############"
PHONE_NUMBER = "##############"

driver.get(r"https://www.linkedin.com/jobs/search/?f_AL=true&geoId=106057199&keywords=python%20developer&location=Brasil&sortBy=R")

login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_btn.click()

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(MY_EMAIL)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)


confirm_login_btn = driver.find_element(By.TAG_NAME, "button")
confirm_login_btn.click()
time.sleep(20)

apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
apply_button.click()

phone_number_input = driver.find_element(By.TAG_NAME, "input")
phone_number_input.send_keys(PHONE_NUMBER)

confirm_button = driver.find_element(By.CSS_SELECTOR, "footer div button")
confirm_button.click()


resume_confirm_button = driver.find_element(By.ID, "ember366")
resume_confirm_button.click()


