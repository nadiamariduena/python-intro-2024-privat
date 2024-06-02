# lang stands for language
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German":  "Hallo"
    }
    #
    msg = f"{greetings[lang]} {name}"
    # In Python, square brackets [] are used to access elements from a dictionary using their keys. In this code, greetings is a dictionary where each language (key) is associated with its respective greeting (value).
    print(msg)