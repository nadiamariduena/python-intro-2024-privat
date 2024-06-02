# import argparse


# parser = argparse.ArgumentParser(  description='Provides a personal greeting.')

# parser.add_argument(
#     #-n: its short for name
#     '_n', '--name', metavar="name",
#     required=True, help="The name of the person to greet."
# )

# args = parser.parse_args()

# msg = f"Hello {args.name}!"
# print(msg)
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




#---------
import argparse

parser = argparse.ArgumentParser(description='Provides a personal greeting.')

parser.add_argument(
    '-n', "--name", metavar="name",
    required=True, help="The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello, {args.name}!"
print(msg)

# --- result
#🖐️ you will get the below error when typing this on your VS terminal:python3 argsParse.py , the reason for that is because you are missing to add a value/name
#
# result
# usage: argsParse.py [-h] -n name
# argsParse.py: error: the following arguments are required: -n/--name

# ----- add the value / name into the console/type the below:
#python3  argsParse1.py -n "I am typing the value name which is Nathaly"
#
#result
#Hello I am typing the value name which is Nathaly!
