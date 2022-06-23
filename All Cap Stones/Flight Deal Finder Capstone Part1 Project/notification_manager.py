import smtplib
from flight_data import FlightData

EMAIL = ""
PASSWORD = ""


class NotificationManager:
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD


    def sendMessage(self, FlightData:FlightData):
        with smtplib.SMTP("smtp.google.com", 587, timeout= 120) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.send_message(
                from_addr= self.email,
                to_addrs= self.email,
                msg= "Hey! Low Price Flight Alert! \n\n"
                f"Only {FlightData.getPrice} to fly from {FlightData.departure_city}-{FlightData.departure_airport_code}"
                f" to {FlightData.arrival_city}-{FlightData.arrival_airport_code}."
            )

            
        