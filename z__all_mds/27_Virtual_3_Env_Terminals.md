## Several Virtual Environments


- I was testing the virtual environments using different **Python versions** simultaneously, and i notice that you have to be careful in the way you do it.



<br>
<br>

- ✋ I recommend you check the python version  within the **bin** (that is generated within the **.venv** folder), here: `.venv/bin` , you should find something like (pip3, python3.10 or whatever version you had at the moment of creating the venv folder), HERE COMES the interesting:


<br>

#### I created a `.venv` in each terminal


<br>

1 🔸 Open the **Weather.py** (so that you can change the **interpreter** by clicking at the bottom right of your VS, once you click on it you will see at the top of your VS code a dropdown with all the python versions that you should have already installed with **pyenv** )


```javascript
 _____________________________________________________________
|  python 3.8.18      |   python  3.10.8   |  python 3.7.14
|                     |                    |
|                     |                    |
|    Terminal 1             Terminal 2     |     Terminal 3   |
|---------------------|---------------------------------------|

//
Terminal 1 will handle LESSON_1
Terminal 2 (child of terminal 1) will handle LESSON_2
//
// it should look like this:
mycomputer@userLudovico:~/lesson-1$
mycomputer@userLudovico:~/lesson-2$
```

<br>

2 🔸 Lets say you have only **Terminal 1** open, this terminal is **cd** within **LESSON_1**  (you shouldn't have any other terminal open within your VS code for this test)


<br>

3 🔸 In this terminal you have **python 3.8.18** marked at the bottom right, if you decided to open a second window based on this terminal 1 (look at the right bar, and hover on the terminal 1, click on the option **split** that looks like a window, this will create a child terminal, therefore split)


4 🔸 Even if you changed the **interpreter** now, lets say for a **version 3.7.14** , you will see that once you have generated the **venv folder** within **LESSON_2** (terminal 2), you will still get the **python 3.8.18**


<br>
<br>

### 🌈 You should not open a second terminal like this, click on the `+` (right bottom bar) instead, only like that you can be sure you are going to get the right version, the version you have currently within your INTERPRETER


- DELETE your venv

```javascript
// 1  (in case you venv is activated)
deactivate
// 2 remove
rm -rf .venv
// create again but this time open the terminal using the + PLUS
python -m venv .venv
// CHECK the PYTHON version within the bin and if the python version matches the one on YOUR INTERPRETER then proceed to ACTIVATE
// activate
source .venv/bin/activate
```
