## 🟡 Weather API

- this is a continuation of the **DOTENV** setup: [click here to be redirected there](./z__all_mds/27_Virtual_3_Environments_other-packages.md)

>Once you have clicked on the above link, click on the **"Dotenv   [Go to section]"** there you will catch up about the topic





<br>
<br>

### 🟣 STEPS:

- create an account **here**: https://home.openweathermap.org/

- confirm the email

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