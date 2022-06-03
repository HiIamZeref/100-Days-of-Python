import requests
from datetime import datetime
import smtplib

MY_LAT = -3.732714 # Your latitude
MY_LONG = -38.526997 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def checkPosition(my_lat, my_long, check_lat, check_long):
    lat_check = False
    long_check = False

    check = False

    if (check_lat <= (my_lat + 5)) and (check_lat >= (my_lat - 5)):
        lat_check = True
    
    if check_long <= (my_long + 5) and check_long >= (my_long - 5):
        long_check = True

    
    if lat_check and long_check:
        check = True

    return check

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())

time_hour = time_now.split()[1].split(":")[0]

print(time_hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



