import requests
from dotenv import load_dotenv
# you will see the red underline under the imports, until you start creating the functions
import os


load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")


    request_url = "https://api.openweathermap.org/data/2.5/weather?appid={API key}&units=imperial"