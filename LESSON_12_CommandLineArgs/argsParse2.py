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
    #
    #So, when you write greetings[lang], Python looks up the value associated with the key lang in the greetings dictionary. The lang variable contains the language passed to the function hello(), and it's used as the key to retrieve the appropriate greeting from the greetings dictionary.
    #
    print(msg)