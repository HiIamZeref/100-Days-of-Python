import requests

api_adress = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9eb26fe6ae64cd0e0ff9355ca7b0662e"

params = {
    "lat": -3.732714,
    "lon": -38.526997,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(api_adress, params=params)
response.raise_for_status()
data = response.json()

hourly = data["hourly"][:12]

ids = []
will_rain = False

for hour in hourly:
    id = hour["weather"][0]["id"]

    if id < 700:
        will_rain = True
        
    ids.append(id)

if will_rain:
    print("Bring an umbrella.")




    
    
