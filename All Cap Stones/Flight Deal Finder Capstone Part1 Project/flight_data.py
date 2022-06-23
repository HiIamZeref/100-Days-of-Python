class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        for info in data:
            self.price = info['price'] 
            self.departure_city =  info['cityFrom']
            self.departure_airport_code = info['flyFrom']
            self.arrival_city = info['cityTo']
            self.arrival_airport_code = info['flyTo'] 
            #outbound_date =
            #inbound_date" =

    def getPrice(self):
        return float(self.price)
        

        


        
        