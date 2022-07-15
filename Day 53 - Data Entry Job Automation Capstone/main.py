from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

forms_url = "https://forms.gle/kqzbMDJRMm31B2X88"
zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3Anull%2C"mapBounds"%3A%7B"west"%3A-122.56276167822266%2C"east"%3A-122.30389632177734%2C"south"%3A37.69261345230467%2C"north"%3A37.857877098316834%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fr"%3A%7B"value"%3Atrue%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"pmf"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12%7D'
request_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75",
    "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
chrome_driver_path = 'D:\Development\chromedriver.exe'

response = requests.get(url=zillow_url, headers= request_headers)
website = response.text

soup =  BeautifulSoup(website, "html.parser")



#PRICE LINK & ADDRESS
#GET ALL PRICES
all_price_tags = soup.find_all(name="div", class_= "list-card-price")
all_prices = []
for tag in all_price_tags:
    all_prices.append(tag.getText())

#GET ALL LINKS:
all_link_tags = soup.find_all(name= "a", class_="list-card-link")
all_links = []
for tag in all_link_tags:
    all_links.append(tag['href'])

#GET ALL ADDRESSES
all_addresses_tags = soup.find_all(name= "address", class_="list-card-addr")
all_adresses = []
for tag in all_addresses_tags:
    all_adresses.append(tag.getText())


#COMPLETE FORM

driver = webdriver.Chrome(chrome_driver_path)
driver.get(forms_url)
sleep(2)
for price in all_prices:
    index = all_prices.index(price)

    #INPUT ADDRESS
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(all_adresses[index])

    #INPUT PRICE
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price)

    #LINK INPUT
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(all_links[index])

    #PRESS SEND
    send_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send_btn.click()

    #GO AGAIN
    retry = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    retry.click()
    sleep(5)

