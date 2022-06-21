import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT = 72
HEIGHT = 174
AGE =  20


#SENSITIVE DATA
APP_ID = "###########3"
API_KEY = "###################"
SHEETY_AUTORIZATION = "##############"

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2afe7f5eab7fa65a07a136a1a2a73fa9/meuTreino/workouts"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    
}

sheety_headers = {
    "Authorization": SHEETY_AUTORIZATION
}


exercise_text = input("Tell me which exercises you did.")

natural_exercise_json = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

natural_exercise_response = requests.post(url=natural_exercise_endpoint, json= natural_exercise_json, headers= nutritionix_headers)
exercise_data = natural_exercise_response.json()

exercises = exercise_data["exercises"]
print(exercises)



for exercise in exercises:
    today = datetime.now()
    formated_day = today.strftime("%d/%m/%Y")
    formated_hours = today.strftime("%H:%M:%S")

    sheety_params = {
        "workout": {
            "date": formated_day,
            "time": formated_hours,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json= sheety_params, headers=sheety_headers)
    print(sheety_response.text)