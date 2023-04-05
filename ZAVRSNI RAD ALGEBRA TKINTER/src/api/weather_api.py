# import json
# import requests
# from src.utils.datetime_utils import formatted_date, formatted_time
# import random


# class WeatherForecast:
#     def __init__(self, city):
#         self.url = f"https://weatherdbi.herokuapp.com/data/weather/{city}"
#         self.fallback_url = f"https://api.open-meteo.com/v1/forecast?latitude=45.79&longitude=15.96&current_weather=true&hourly=relativehumidity_2m"
#         self.is_using_fallback = False
#         self.data = None
#         self.send_request()

#     def send_request(self):
#         #response = requests.get(self.url)
#         response = requests.get(self.url, verify=False)
#         if response.status_code == 200:
#             self.data = json.loads(response.text)
#         else:
#             self.is_using_fallback = True
#             response = requests.get(self.fallback_url)
#             if response.status_code == 200:
#                 self.data = json.loads(response.text)
#             else:
#                 self.data = {
#                     "region": self.city,
#                     "currentConditions": {
#                         "temp": {
#                             "c": round(random.uniform(0, 40), 2)
#                         },
#                         "humidity": round(random.uniform(30, 70), 2),
#                         "comment": "Unknown"
#                     }
#                 }

#     def get_formatted_weather_data(self):
#         if self.is_using_fallback and self.is_using_fallback == True:
#             return {
#                 "location": "Zagreb",
#                 "current_temperature": self.data["current_weather"]["temperature"],
#                 "humidity": self.data["hourly"]["relativehumidity_2m"][0],
#                 "description": "Fallback API - no desc",
#                 "last_refresh": f"{formatted_date()} {formatted_time()}"
#             }
#         else:
#             return {
#                 "location": self.data["region"],
#                 "current_temperature": self.data["currentConditions"]["temp"]["c"],
#                 "humidity": self.data["currentConditions"]["humidity"],
#                 "description": self.data["currentConditions"]["comment"],
#                 "last_refresh": f"{formatted_date()} {formatted_time()}"
#             }
import random
from src.utils.datetime_utils import formatted_date, formatted_time

class WeatherForecast:
    def __init__(self, city):
        self.city = city
        self.data = self.generate_random_data()
    
    def generate_random_data(self):
        return {
            "region": self.city,
            "currentConditions": {
                "temp": {
                    "c": round(random.uniform(0, 40), 2)
                },
                "humidity": round(random.uniform(30, 70), 2),
                "comment": random.choice(["Sunny", "Cloudy", "Rainy"])
            }
        }

    def get_formatted_weather_data(self):
        return {
            "location": self.data["region"],
            "current_temperature": self.data["currentConditions"]["temp"]["c"],
            "humidity": self.data["currentConditions"]["humidity"],
            "description": self.data["currentConditions"]["comment"],
            "last_refresh": f"{formatted_date()} {formatted_time()}"
        }
