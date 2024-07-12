## Several Virtual Environments


- I was testing the virtual environments using different **Python versions** simultaneously, and i notice that you have to be careful in the way you do it.



<br>
<br>

- ✋ I recommend you check the python version  within the **bin** (that is generated within the **.venv** folder), here: `.venv/bin` , you should find something like (pip3, python3.10 or whatever version you had at the moment of creating the venv folder), HERE COMES the interesting:


<br>

#### I created a `.venv` in each terminal


<br>

1 🔸 Open the **Weather.py** (so that you can change the **interpreter** by clicking at the bottom right of your VS, once you click on it you will see at the top of your VS code a dropdown with all the python versions that you should have already installed with **pyenv** )


2 🔸 Lets say you have only **Terminal 1** open (you shouldn't have any other terminal open within your VS code for this test), in this terminal you have **python 3.8.18** marked at the bottom right, if you decided to open a second window based on this terminal 1 (look at the right bar, and hover on the terminal 1, click on the option **split** that looks like a window, this will create a child terminal, therefore split), even if you changed the **interpreter** now, lets say for a **version 3.7.14**


```javascript
 _____________________________________________________________
|  python 3.8.18      |   python  3.10.8   |  python 3.7.14
|                     |                    |
|                     |                    |
|    Terminal 1             Terminal 2     |     Terminal 3   |
|---------------------|---------------------------------------|


```