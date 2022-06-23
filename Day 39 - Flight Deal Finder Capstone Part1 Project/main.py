#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

sheet = DataManager()
sheet_data = sheet.getSheetData()


flight_search = FlightSearch(sheet_data)
#sheet.updateData(flight_search.flight_data)

pprint(flight_search.flight_data)
flight_search.comparePrices()

