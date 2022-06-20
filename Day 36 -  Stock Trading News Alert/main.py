import requests
import smtplib

EMAIL = "########"
PASSWORD = "#######"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "#########"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "outputsize":"compact",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY =  "##########"

news_params = {
    "apikey": NEWS_KEY,
    "q": COMPANY_NAME
}

    

response_stock = requests.get(STOCK_ENDPOINT, stock_params)
response_stock.raise_for_status()
stock_data = response_stock.json()

r_news = requests.get(NEWS_ENDPOINT, news_params)
r_news.raise_for_status()
news_data = r_news.json()

print(news_data)

daily_data = stock_data["Time Series (Daily)"]

close_stock_prices = [day["4. close"] for (key,day) in daily_data.items()]

difference = abs(float(close_stock_prices[0]) - float(close_stock_prices[1]))
print(difference)

percentage_difference = (difference/(float(close_stock_prices[0])))*100
print(percentage_difference)



if percentage_difference > 5:
    articles = news_data["articles"][:3]

    headlines_descriptions = [[article["title"], article["description"]] for article in articles]

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)

        for news in headlines_descriptions:
            connection.sendmail(
                from_addr= EMAIL,
                to_addrs= EMAIL,
                msg= f"Headline: {news[0]} \n\n Brief: {news[1]}"
            )


