import requests

SHETTY_ENDPOINT = "https://api.sheety.co/2afe7f5eab7fa65a07a136a1a2a73fa9/flightDeals/prices"
TOKEN = "################" 


class DataManager:
    def __init__(self):
        self.sheety_endpoint = SHETTY_ENDPOINT
        self.header = {
            "Authorization": TOKEN
        }        

    def getSheetData(self):
        response = requests.get(url= self.sheety_endpoint, headers= self.header)
        response.raise_for_status()
        brute_data = response.json()
        return brute_data["prices"]


    def updateData(self, new_Data):
        for data in new_Data:

            row = {
                "price": data
            }

            response = requests.put(url=f"{self.sheety_endpoint}/{data['id']}", headers= self.header, json=row)
            

        

