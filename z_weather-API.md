## 🟡 Weather API

- this is a continuation of the **DOTENV** setup: [click here to be redirected there](./z__all_mds/27_Virtual_3_Environments_other-packages.md)

>Once you have clicked on the above link, click on the **"Dotenv   [Go to section]"** there you will catch up about the topic





<br>
<br>

### STEPS:

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


- CREATE a new file, name it **weather.py**

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