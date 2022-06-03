import smtplib
import random
import datetime as dt

today = dt.datetime.now()


with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    

print(today.weekday())

my_email = "######"
password = "######"

if today.weekday() == 3:
    phrase = all_quotes[random.randint(0, len(all_quotes) - 1)]
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="raissa.rib004@gmail.com", 
            msg=f"Subject: Frase motivacional do dia! \n\n {phrase}"
        ) 