
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "######"
my_password = "######"







today = dt.datetime.now()
today_tuple = (today.month, today.day)



birthdays_data = pd.read_csv("birthdays.csv")



birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in birthdays_data.iterrows()}
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]



if today_tuple in birthdays_dict:
    choose_path = random.choice(letters)
    
    
    with open(f"letter_templates\{choose_path}") as chosen_letter:
        string = "".join(chosen_letter)
        birthday_message = string.replace("[NAME]", birthdays_dict[today_tuple]["name"])

    
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg= "Subject: Happy Birhtday!! \n\n " + birthday_message
        )
        













