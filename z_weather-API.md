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

<br>

# 🟠 PPRINT

 Now lets import another **module**, its called **PPRINT**

<br>

**PPRINT** stands for **"pretty-print"**  💅and it is both a module and a function within Python.

- Its primary **purpose** is to **format** complex **Python** data **structures** in a more **readable** way,  **especially** when they are **nested** or contain multiple levels of **indentation** ✋.

<br>

### 🫐 Module and Function

**Module:** The  pprint module (pprint) in Python provides the pprint() function and related utilities.

 - - <u>It is used **to print data structures** such as **dictionaries and lists** in a visually appealing and readable format</u> , making it easier for humans to interpret.

- **Function:** The pprint() function within the module is the main tool used for this purpose.

- - It takes a Python data structure as input and outputs a formatted representation of that structure.

- - This can include **indenting** nested structures, **breaking** long **lines**, and generally presenting the data in a way that is easier to understand than the default print() function output.



<br>
<br>

## 🟧 Use it on the `weather.py`

 Now lets import the **PPRINT** within the weather app

 <br>


```python
from pprint import pprint
```

#### use it

- once imported , replace the default print by the pprint

```python
# before
 print(weather_data)

# after
pprint(weather_data)
```

<br>

- 🌈 RUN the code with the arrow at the top bar of your VS code


<br>

### Output

```javascript
// ✋ BEFORE PPRINT
{'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 73.72, 'feels_like': 74.98, 'temp_min': 70.57, 'temp_max': 75.49, 'pressure': 1017, 'humidity': 89, 'sea_level': 1017, 'grnd_level': 1013}, 'visibility': 10000, 'wind': {'speed': 8.05, 'deg': 210}, 'clouds': {'all': 20}, 'dt': 1720930800, 'sys': {'type': 2, 'id': 2013408, 'country': 'US', 'sunrise': 1720948810, 'sunset': 1721002783}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}


#
#
// ✅ after PPRINT

*** Get Current Weather Conditions ***


Please enter a city name:
New Mexico
{'base': 'stations',
 'clouds': {'all': 1},
 'cod': 200,
 'coord': {'lat': 34.5003, 'lon': -106.0008},
 'dt': 1720985736,
 'id': 5481136,
 'main': {'feels_like': 88.54,
          'grnd_level': 812,
          'humidity': 13,
          'pressure': 1015,
          'sea_level': 1015,
          'temp': 92.98,
          'temp_max': 93.06,
          'temp_min': 91.33},
 'name': 'New Mexico',
 'sys': {'country': 'US',
         'id': 2003420,
         'sunrise': 1720958529,
         'sunset': 1721009837,
         'type': 2},
 'timezone': -21600,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 109, 'gust': 13.11, 'speed': 8.57}}
```

<br>
<br>

## 👾 [Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=lG0Ylgi4eziYe_MY&t=1550)

### export it

- If I want to export it as a module i have to add the

```python
__name__ == "__main__"
```

#### like here below:

```python
if __name__ == "__main__":
    get_current_weather()
```

<br>
<br>

## 🟠 Reach specific properties from the result below:


```javascript
Las Vegas
{'base': 'stations',
 'clouds': {'all': 0},
 'cod': 200,
 'coord': {'lat': 36.175, 'lon': -115.1372},
 'dt': 1720996842,
 'id': 5506956,
 'main': {'feels_like': 99.66,
          'grnd_level': 946,
          'humidity': 14,
          'pressure': 1011,
          'sea_level': 1011,
          'temp': 103.69,
          'temp_max': 104.68,
          'temp_min': 102.56},
 'name': 'Las Vegas',
 'sys': {'country': 'US',
         'id': 6171,
         'sunrise': 1720960467,
         'sunset': 1721012285,
         'type': 1},
 'timezone': -25200,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 180, 'gust': 21.85, 'speed': 14.97}}
```


<br>

 ### 🍭 Showing specific properties

- Here i will focus on reaching the **name** property from the above **object** ⤴️  (**keep in mind that the data is constantly changing** , so you might have to review the object all the time when testing)

```python
 print(f'\nCurrent weather from {weather_data["name"]}')

```

 <br>


 #### like so


```python
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    weather_data = requests.get(request_url).json()

    # hide this --- before using the pprint:
    #  pprint(weather_data)
    #

    # hide this --- using the "pprint" to beautify the code (the result will be well structured and indented)
    # pprint(weather_data)


    print(f'\nCurrent weather from {weather_data["name"]} 🚀')




if __name__ == "__main__":
    get_current_weather()
```

### output

```python
*** Get Current Weather Conditions ***


Please enter a city name:
miami

Current weather from Miami 🚀
```

<br>

### 🟣 Reach a property child from an object

- from the code below, i am going to grab the **main** and then one of the **children of the main**, in this case the **temp**

```javascript
Miami
{'base': 'stations',
 'clouds': {'all': 40},
 'cod': 200,
 'coord': {'lat': 25.7743, 'lon': -80.1937},
 'dt': 1721013926,
 'id': 4164138,
 'main': {'feels_like': 93.74, ✋
          'grnd_level': 1019,
          'humidity': 80,
          'pressure': 1019,
          'sea_level': 1019,
          'temp': 83.91, ✋
          'temp_max': 85.01,
          'temp_min': 82},
 'name': 'Miami',
 'sys': {'country': 'US',
         'id': 2009435,
         'sunrise': 1720953504,
         'sunset': 1721002474,
         'type': 2},
 'timezone': -14400,
 'visibility': 10000,
 'weather': [{'description': 'scattered clouds',
              'icon': '03n',
              'id': 802,
              'main': 'Clouds'}],
 'wind': {'deg': 90, 'speed': 10.36}}
```





#### output

```javascript
// Please enter a city name:
// Miami

The temp/temperature weather is 83.91 // reaching the parent: main and then the child: temp
```
<br>
<br>

### 🟣 Reach a property child from an array `["weather"][0]}`

```javascript

    print(f'\nFEELS like 🌻  {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]}')
```


#### output

<br>

```javascript
// Please enter a city name:
// Miami

FEELS like 🌻  93.54 and {'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}


// in the object you see it like here

/*

 'weather': [{'description': 'scattered clouds',
              'icon': '03n',
              'id': 802,
              'main': 'Clouds'}],
*/
```