from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "################"
PASSWORD = "#################"

chrome_driver_path = 'D:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://tinder.com/")

login_btn = driver.find_element(By.CLASS_NAME, "button")
login_btn.click()

accept_cokkies_btn = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cokkies_btn.click()
time.sleep(5)

facebook_login_btn = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login_btn.click()
time.sleep(15)

base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]

driver.switch_to.window(facebook_window)

email_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(10)


driver.switch_to.window(base_window)
time.sleep(10)

allow_gps = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]')
allow_gps.click()
time.sleep(5)

not_interessed = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[2]')
not_interessed.click()
time.sleep(10)

pass_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
for i in range(100):
    pass_button.click()
    time.sleep(2)   
