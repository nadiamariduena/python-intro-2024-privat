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

<br>

### if you have a file within a folder

- check if you are at the root

- if you are on the root type **ls** to visualize all the folders in this project, you will see something like this:

```javascript
// - this is the content of my folder to learn python
// - i need to enter the folder LESSON_12_CommandLineArgs", for that i need to type on the visual studio terminal "cd LESSON_12_CommandLineArgs" (presuming i am on the root)
// ⚠️ careful with spaces, the folder containing the file argsParse1.py , shouldnt have spaces otherwise it wont work. by spaces i mean it should look like this here below: "LESSON_12_CommandLineArgs" and not "LESSON_12_CommandLineArgs "
 argsParse.py          LESSON_12_CommandLineArgs   z__all_mds
 img                   LESSON_5_loops             'z_args_&_kwargs.md'
 LESSON_01             LESSON_6_Functions          z_floating.md
 LESSON_02             LESSON_7_recursion          z_identation-issues.md
 LESSON_03_tuples      LESSON_8_Scope              z__modules-methods.md
 LESSON_04_dictio      LESSON_9_closures           z__smallTips.md
 LESSON_10_f_Strings   MORE-memory.md
 LESSON_11_modules     README.md

```

#### once you cd on the LESSON_12_CommandLineArgs

- type on the visual studio terminal: `python3 argsParse1.py`

```javascript
// this is how it should look like,
/python-intro-2024-privat/LESSON_12_CommandLineArgs$ python3 argsParse1.py ✋
```
