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

# NAME parser
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

# LANGUAGE parser
    parser.add_argument(
        "-l", "lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )
