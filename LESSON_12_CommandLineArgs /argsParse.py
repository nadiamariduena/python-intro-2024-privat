import argsParse


parser = argsParse.ArgumentParser(
    description='Provides a personal greeting.'
)

parser.add_argument(
    #-n: its short for name
    '_n', '--name', metavar="name",
    required=True, help="The name of the person to greet."
)