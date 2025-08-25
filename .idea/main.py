import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY=os.environ["API_KEY"]
SHEET_AUTH=os.environ["SHEET_AUTH"]

exercises=input("Tell me which exercises you did today?\n")

headers={
    'x-app-id': APP_ID ,
    'x-app-key': API_KEY
}

nutrition_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_config={
    "query": exercises
}

response= requests.post(url=nutrition_endpoint,json=nutrition_config,headers=headers)
data=response.json()

exercise=data['exercises'][0]["name"]
duration=data['exercises'][0]['duration_min']
calories=data['exercises'][0]['nf_calories']


today=datetime.now()
day=today.strftime("%d/%m/%Y")
time=today.strftime("%X")


sheety_endpoint="https://api.sheety.co/a1766fc2644a9b2d9231c523cdc7a83f/myWorkouts/workouts"
sheety_add={
    'workout': {'date': day,
                  'time': time,
                  'exercise': exercise,
                  'duration': duration,
                  'calories': calories,
                  }
}

headers={
    "Authorization": SHEET_AUTH
}

response=requests.post(url=sheety_endpoint,json=sheety_add,headers=headers)
print(response.text)