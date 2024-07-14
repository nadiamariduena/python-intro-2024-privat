## 🟡 Weather API

- this is a continuation of the **DOTENV** setup: [click here to be redirected there](./z__all_mds/27_Virtual_3_Environments_other-packages.md)

>Once you have clicked on the above link, click on the **"Dotenv   [Go to section]"** there you will catch up about the topic





<br>
<br>

### 🟣 STEPS:

- create an account **here**: https://home.openweathermap.org/

- confirm the email

-You will receive an confirmation email, then you will receive a second email that says

```javascript
// API key:
// - Within the next couple of hours, your API key:
// 62523871...your api will be activated and ready to use
// - You can later create more API keys on your account page
// - Please, always use your API key in each API call
```

<br>

- go to the  **API keys** page:  https://home.openweathermap.org/api_keys

- copy the key

- create an `.env` file (**but** if you already called your environment folder **.env** , choose something else), i will call mine `.myenv` , 🔴 **DONT commit/PUSH** until you have added it to the `.gitignore` file, but if you have already create it, you will have to either use git command to remove it from the remote, or delete the **myenv** on your local and create it again

- within the `.myenv` file , add the **key**:

```javascript
// add your own key here
API_KEY=6452136...more
```


- CREATE a new file, call it **weather.py**

<br>
<br>

### 🍰 The structure

- after you read about the DOTENV and followed the steps there: [DOTENV intro](./z__all_mds/27_Virtual_3_Environments_other-packages.md), you should have the following

```javascript
project_folder/
├── env/
├── .gitignore/
├── .myenv/
├── requirements.txt/
└── weather.py/ // create this ✋

```

<br>
<br>

###  🟣 Continue with the steps:

<br>

-  🍊 **Go back to the weather API** page, and click on the API link (top bar) or click here: [openweathermap.org/api](https://openweathermap.org/api)



- Once there, scroll down and look for the **current weather data**

- click on the grey button that says   [API doc](https://openweathermap.org/current)

<br>

#### Once there [API doc](https://openweathermap.org/current) ,  you will find this url BELOW (We will be modifying this)


### 🔸 lat & lon

```javascript
// - You can provide a city instead of lat (latitude) or lon (longitude)
// read more here: https://openweathermap.org/current
// ✋
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
```

<br>

### 🔸 units of measure

- at the right side of the page  [API doc](https://openweathermap.org/current) (at the bottom) , you will find the **units of measure**, click here: [current#data](https://openweathermap.org/current#data)

<br>

##### there you will see something like this:

**Units of measurement**

`standard`, `metric`, and `imperial` units are available.  [List of all API parameters with available units](https://openweathermap.org/weather-data).

**Parameters**

`units`	optional	`standard`, `metric`, `imperial`. When you do not use the `units` parameter, format is `standard` by default.

<br>

```python
# Temperature is available in Fahrenheit, Celsius and Kelvin units.

For temperature in Fahrenheit use units=imperial

For temperature in Celsius use units=metric

//
Temperature in Kelvin is used by default, no need to use units parameter in API call

//
# List of all API parameters with units openweathermap.org/weather-data
```

###  🟣 Continue with the steps:

- Within the `weather.py` , create a new variable, call it: **request_url** like so: `request_url = "add the weather url here"`

<br>

```javascript
// before mods
request_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

// after modification
request_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=imperial"
```


 #### like so:

 - At this point, my machine will not recognize the dotenv or the charset-normalizer==3.3.2, packages installed on the environment, to check the packages, inspect the **requirements.txt**

 ```python
import requests
from dotenv import load_dotenv
import os

request_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=imperial"
 ```

 #### issues with the DOTENV installation

 ```javascript
certifi==2024.7.4
charset-normalizer==3.3.2 ✋
idna==3.7
python-dotenv==1.0.1 ✋
requests==2.32.3
urllib3==2.2.2
 ```

<br>

 ### 🌈 solution: [INSTALL PYENV](./z_PYENV_installing.md)


<br>
<br>
<br>


 ## 🟢 Let's continue


- Here below you can notice that i grab the API KEY, that is coming from the `.env`, there i have the long key from the weather site `{os.getenv("API_KEY")}`

<br>

 ```python
# before
request_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=imperial"
#
#
#
# ✋ after
# this below will deactivate temporarly the red underline
## pylint: disable=import-error

import requests
from dotenv import load_dotenv
# i made it work even with the red underline, so i presume it has to do with the python version i am using, i will test it more later on
#
import os

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")


    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    print(request_url)

get_current_weather()
```

<br>

### to LAUNCH it

- 🔴 type this on the console of the project where you have your environment ACTIVATED


```javascript
// my project is LESSON17
python Weather.py
```

#### like so

```javascript
(.venv) mycomputer@usercomputer:~/python-intro-2024-privat/LESSON_17_Virtual_Environment_and_pip$ python Weather.py
```

### RESULT

- in your console you will be required to add a city

```javascript
*** Get Current Weather Conditions ***


Please enter a city name:
// i typed
Arizona
```

#### after i typed a city name, it generated this link (you can copy and paste it to your browser)

```javascript
https://api.openweathermap.org/data/2.5/weather?appid=620..........myAPI&q=Arizona&units=imperial
```

<br>

#### on your browser you will see the following data

- if you want to see the data in a clean way, install this [json-viewer  EXTENSION](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?pli=1)

```python
{"coord":{"lon":-111.501,"lat":34.5003},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":81.91,"feels_like":79.56,"temp_min":79.14,"temp_max":85.28,"pressure":1011,"humidity":12,"sea_level":1011,"grnd_level":811},"visibility":10000,"wind":{"speed":9.6,"deg":62,"gust":18.5},"clouds":{"all":0},"dt":1720495145,"sys":{"type":1,"id":5309,"country":"US","sunrise":1720441237,"sunset":1720492879},"timezone":-25200,"id":5551752,"name":"Arizona","cod":200}

```

<br>

### with JSON viewer

```javascript

{
  "coord": {
    "lon": -111.501,
    "lat": 34.5003
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 81.91,
    "feels_like": 79.56,
    "temp_min": 79.14,
    "temp_max": 85.28,
    "pressure": 1011,
    "humidity": 12,
    "sea_level": 1011,
    "grnd_level": 811
  },
  "visibility": 10000,
  "wind": {
    "speed": 9.6,
    "deg": 62,
    "gust": 18.5
  },
  "clouds": {
    "all": 0
  },
  "dt": 1720495145,
  "sys": {
    "type": 1,
    "id": 5309,
    "country": "US",
    "sunrise": 1720441237,
    "sunset": 1720492879
  },
  "timezone": -25200,
  "id": 5551752,
  "name": "Arizona",
  "cod": 200
}
```
#### now lets check ARIZONA

- look for **arizona longitude and latitude** in your browser

```javascript
Arizona/Coordinates
34.0489° N, 111.0937° W
Arizona, USA Lat Long Coordinates Info
The latitude of Arizona, USA is 34.048927, and the longitude is -111.093735. Arizona, USA is located at United States country in the States place category with the gps coordinates of 34° 2' 56.1372'' N and 111° 5' 37.4460'' W.
```


### But lets continue with the code

- I will be using JSON to show the data within the VS code terminal

- run the code by clicking on the top bar (look for the arrow), once you run the code you will have the code on step 1, then after you type the city, you will have the outcome in step 2


```javascript
// step 1
*** Get Current Weather Conditions ***


Please enter a city name:
Boston


// step 1
// OUTPUT ✋
{'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 73.72, 'feels_like': 74.98, 'temp_min': 70.57, 'temp_max': 75.49, 'pressure': 1017, 'humidity': 89, 'sea_level': 1017, 'grnd_level': 1013}, 'visibility': 10000, 'wind': {'speed': 8.05, 'deg': 210}, 'clouds': {'all': 20}, 'dt': 1720930800, 'sys': {'type': 2, 'id': 2013408, 'country': 'US', 'sunrise': 1720948810, 'sunset': 1721002783}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}
```

<br>

<br>

## 🟠 PPRINT

 Now lets import another **module**, its called **PPRINT**

<br>

**pprint** stands for **"pretty-print"**  💅and it is both a module and a function within Python.

- Its primary **purpose** is to **format** complex **Python** data **structures** in a more **readable** way,  **especially** when they are **nested** or contain multiple levels of **indentation** ✋.





