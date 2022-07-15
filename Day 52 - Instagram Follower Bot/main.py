from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from instaFollower import InstaFollower

chrome_driver_path = 'D:\Development\chromedriver.exe'
ACCOUNT = "filipedeschamps"
USERNAME = "#########"
PASSWORD = "########"

insta_bot = InstaFollower(chrome_driver_path, ACCOUNT, USERNAME, PASSWORD)

insta_bot.login()
insta_bot.findFollowers()
insta_bot.follow()