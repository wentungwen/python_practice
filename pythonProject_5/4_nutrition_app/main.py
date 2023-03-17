import requests
import datetime

# dummy_data = json.load(open("./data.json"))["exercises"]
# print(dummy_data)

NUTRI_ID = "bea084f7"
NUTRI_API_KEY = "8549465adb509728066e15172b8539e2"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_URL = "https://api.sheety.co/8bf12b5a57dde61178d59b47bf007694/myWorkouts/workouts"
SHEET_AUTH = "Basic d2VudHVuZ3dlbjp1bzc4aXJ0eQ=="

nutri_header = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_API_KEY,
}

nutri_params = {
    "query": input("What exercise did you do today: "),
    "gender": "female",
    "weight_kg": 50,
    "height_cm": 166,
    "age": 24
}

response = requests.post(url=NUTRI_ENDPOINT, json=nutri_params, headers=nutri_header)
nutri_data = response.json()["exercises"]
print(nutri_data)

now = datetime.datetime.today()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")


sheet_header = {
    "Authorization": "Basic d2VudHVuZ3dlbjp1bzc4aXJ0eQ=="
}
workouts_list = [
    {
        "date": date,
        "time": time,
        "exercise": n["name"].title(),
        "duration": n["duration_min"],
        "calories": n["nf_calories"]
    }
    for n in nutri_data
]

for workout in workouts_list:
    workout_item = {
        "workout": workout
    }
    response_sheet = requests.post(url=SHEET_URL, json=workout_item)
    print(response_sheet.text)
