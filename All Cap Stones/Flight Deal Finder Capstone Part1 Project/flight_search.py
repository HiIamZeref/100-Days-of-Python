from datetime import datetime, timedelta
import requests
from flight_data import FlightData
from pprint import pprint
from notification_manager import NotificationManager

API_KEY = "###########"
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
SEARCH_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    def __init__(self, flight_data):
        self.flight_data = flight_data

        self.headers = {
            "apikey": API_KEY
        }
        self.kiwi_endpoint = KIWI_ENDPOINT
        self.search_flight_endpoint = SEARCH_FLIGHT_ENDPOINT
        
        


        

        for data in flight_data:
            if data["iataCode"] == "":
                params = {
                    "term": data["city"]
                }
                response = requests.get(self.kiwi_endpoint, params= params, headers= self.headers)
                response.raise_for_status()
                response_Data = response.json()["locations"]
                data["iataCode"] = response_Data[0]['code']

    def comparePrices(self):
        for data in self.flight_data:
            lowest_sheet_price = float(data['lowestPrice'])
            

            params = {
                "fly_from": "LON",
                "fly_to": data['iataCode'],
                "date_from": datetime.today().strftime("%d/%m/%Y"),
                "date_to": (datetime.today() + timedelta(180)).strftime("%d/%m/%Y"),
                "curr": "GBP",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "one_for_city": 1,
                "max_stopovers": 0,
            }

            response = requests.get(self.search_flight_endpoint, params= params, headers= self.headers)
            response.raise_for_status()
            response_Data = response.json()
            pprint(response_Data['data'])
            flight_Data = FlightData(response_Data['data'])
            
            lowest_search_price = flight_Data.getPrice()

            if (lowest_sheet_price > lowest_search_price):
                send_email = NotificationManager(flight_Data)
                send_email.sendMessage()




            

    
                    

        
    