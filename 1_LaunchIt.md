## Launching it

- withing your VS, type this to check the version

```javascript
python3 --version
// result
// Python 3.8.10
```

### check the video and on min [7:36](https://youtu.be/6i3e-j3wSf0?feature=shared&t=456) you will get the below information by typing this `py`

```javascript
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

🔴 But it didnt work for me, I had to do this

```javascript
// open you global terminal on this path (replace it yours)
// hello@kitty:~/Downloads/Python-3.12.0$
// type this:
sudo apt-get install python-is-python3
```

### Now if i type `python` within my VS terminal i get this

```javascript
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

> 🌈 So everytime you want to use this, type `python` on your VS terminal

<br>

https://askubuntu.com/questions/1144446/python-installed-in-ubuntu-but-python-command-not-found

### Try the following `2 + 2`:

```javascript
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
```

<br>

#### to get out, type `quit()`

<br>

```javascript
Python 3.8.10 (default, Nov 22 2023, 10:22:35)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

<br>

<br>

---

<br>

<br>

## 🍭 Create a FILE

format: `.py`

#### like so

```javascript
someFile.py;
```

#### within the file add this

```javascript
greeting = "Hello world!";
print(greeting);
```

### to run the code

#### option 1

- check at the top right of the `someFile.py` you will see am arrow, click to unfold and select **run python file**

> **IF YOU NOTICE** within your VS terminal you have now a python terminal

<br>

#### option 1

- Type in your terminal

```javascript
// on the video tutorial
py someFile.py // (or whatever you python file name is)
//
// In my case my file is named hello.py and in my comp i use python and not the py, like so
python hello.py
// result
Hello world!
```
