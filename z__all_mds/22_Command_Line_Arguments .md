```python
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
