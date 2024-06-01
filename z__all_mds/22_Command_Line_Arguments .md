## CommandLineArgs

- To test this I will not run the code with the **run** arrow at the top, this time i will have to open the visual studio terminal

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
