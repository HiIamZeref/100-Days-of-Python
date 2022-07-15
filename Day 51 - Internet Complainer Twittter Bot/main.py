from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from internetSpeedTwitterBot import InternetSpeedTwitterBot

LOGIN = "#################"
PASSWORD = "################"


chrome_driver_path = 'D:\Development\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path= chrome_driver_path, chrome_options=options)


twitter_bot = InternetSpeedTwitterBot(driver, LOGIN, PASSWORD)
twitter_bot.get_internet_speed()
twitter_bot.tweet()