import email
from twilio.rest import Client
import smtplib

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

SMTP_EMAIL = "YOUR EMAIL HERE"
SMTP_PASSWORD = "YOUR PASSWORD HERE"



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, customer_email):
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
                connection.starttls()
                connection.login(SMTP_EMAIL, SMTP_PASSWORD)
                connection.send_message(
                    from_addr= SMTP_EMAIL,
                    to_addrs= customer_email,
                    msg=f"New Low Price Flight! \n\n {message}"
                )

