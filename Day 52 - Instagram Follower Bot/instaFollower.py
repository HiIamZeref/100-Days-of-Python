from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaFollower:
    def __init__(self, driver_path: str, account:str, username:str, password:str):
        self.driver = webdriver.Chrome(driver_path)
        self.account = account
        self.username = username
        self.password = password


    def login(self):
        login_url = 'https://www.instagram.com/accounts/login/'
        self.driver.get(login_url)
        sleep(2)

        login_input = self.driver.find_element(By.NAME, 'username')
        login_input.send_keys(self.username)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        sleep(8)

        notification = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
        notification.click()
        sleep(2)


        

    def findFollowers(self):
        self.driver.get(f"https://www.instagram.com/{self.account}/followers")
        sleep(5)
        
    
    def follow(self):
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, "li button")

        for btn in follow_btns:
            btn.click()
            sleep(2)