import requests
from datetime import datetime
NUTRITIONIX_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/af0c1d5e485ad496467ec43e35ef7ea8/myWorkouts/workouts"
WEIGHT_KG = "your weight"
HEIGHT_CM = "your height"
AGE = "your age "
APP_ID = "your id "
API_KEY = "your api key"
parameters = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {

    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=NUTRITIONIX_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]


        }
    }

    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_input,
        auth=("your name",
              "your password")


    )

