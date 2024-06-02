# lang stands for language
# 1)
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German":  "Hallo"
    }
    #
    msg = f"{greetings[lang]} {name}"
    print(msg)

    # 2) import
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personal greeting."
    )

# 3 NAME parser
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

# 4 LANGUAGE parser
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

##
#
# 5 merging the parsers no.3 & no.4
args = parser.parse_args()

# 6
hello(args.name, args.lang)

#
#----- to test it
# type this on your VS console
# python3 argsParse2.py -n "Ludovico" -l "German"
# As you can see above, i type -l for the language i desire the message to be shown
#
# RESULT:
#Hallo Ludovico