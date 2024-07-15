import requests
from dotenv import load_dotenv
# # you will see the red underline under the imports, until you start creating the functions
#
import os

from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")


    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    weather_data = requests.get(request_url).json()

    # before using the pprint:
    #pprint(weather_data)
    #

    # --- using the "pprint" to beautify the code (the result will be well structured and indented)
    # pprint(weather_data)


    # print(f'\nCurrent weather from {weather_data["name"]} 🚀')
    # #
    print(f'\nThe temp/temperature weather is {weather_data["main"]["temp"]}')

if __name__ == "__main__":
    get_current_weather()