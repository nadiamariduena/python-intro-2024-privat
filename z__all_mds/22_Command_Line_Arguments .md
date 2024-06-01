## CommandLineArgs

- To test this I will not run the code with the **run** arrow at the top, this time i will have to open the visual studio terminal:

<br>

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

<br>

```python
# LESSON_12_CommandLineArgs/argsParse1.py
# import argparse

# error version ---
#
# parser = argparse.ArgumentParser(  description='Provides a personal greeting.')

# parser.add_argument(
#     #-n: its short for name
#     '_n', '--name', metavar="name",
#     required=True, help="The name of the person to greet."
# )

# args = parser.parse_args()

# msg = f"Hello {args.name}!"
# print(msg)



#--------- OR
import argparse

parser = argparse.ArgumentParser(description='Provides a personal greeting.')

parser.add_argument(
    '--name', metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)
#
#
# ----- Or

import argparse

parser = argparse.ArgumentParser(description='Provides a personal greeting.')

parser.add_argument(
    '-name', "--name", metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)
```

### Compare results

```python
# 1 wrong
import argparse


parser = argparse.ArgumentParser(  description='Provides a personal greeting.')

parser.add_argument(
    #-n: its short for nam.encode()# i made the mistakes here, i added a dash instead of a minus
    '_n', '--name', metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)
#
# -- result:
# python3 argsParse.py
# Traceback (most recent call last):
#   File "argsParse.py", line 6, in <module>
#     parser.add_argument(
#   File "/usr/lib/python3.8/argparse.py", line 1366, in add_argument
#     kwargs = self._get_optional_kwargs(*args, **kwargs)
#   File "/usr/lib/python3.8/argparse.py", line 1501, in _get_optional_kwargs
#     raise ValueError(msg % args)
# ValueError: invalid option string '_n': must start with a character '-'




# 2 ---------
import argparse

parser = argparse.ArgumentParser(description='Provides a personal greeting.')

parser.add_argument(
    '--name', metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)
#

# --- result
# I added the file on the root to see if it worked, then i pasted this on the VS terminal: python3 argsParse.py
# python3 argsParse.py
# usage: argsParse.py [-h] --name name
# argsParse.py: error: the following arguments are required: --name
#
#
# 3 ---------

#
##---------
import argparse

parser = argparse.ArgumentParser(description='Provides a personal greeting.')

parser.add_argument(
    '-name', "--name", metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)

# --- result
# python3 argsParse.py
# usage: argsParse.py [-h] -n name
# argsParse.py: error: the following arguments are required: -n/--name
```
