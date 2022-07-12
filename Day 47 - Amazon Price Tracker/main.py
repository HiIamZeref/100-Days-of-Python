import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

product_name = "Nintendo Switch"
wish_price = 2500
EMAIL = "#########"
PASSWORD = "###########"


product_url = "https://www.amazon.com.br/Console-Nintendo-Switch-Vermelho-Nacional/dp/B08LF257QB/ref=sr_1_4"
request_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75",
    "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url= product_url, headers= request_headers)
website = response.text

soup = BeautifulSoup(website, "lxml")
price = soup.find(name="span",class_="a-price-whole")

true_price = float(price.getText().strip(","))
if true_price < wish_price:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user= EMAIL, password= PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="PRICE ALERT! \n\n"
            f"Your product {product_name} is under your wished price! ({wish_price}) Check the link: {product_url}"
        )

