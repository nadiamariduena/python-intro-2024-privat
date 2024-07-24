from helper import fashion_ads

def display_fashion_ads(ad):
    """Simmulates displaying an ad.
    """
    print(f"Showing ad: {ad['text']}")
    print(f"Image: {ad['image']}")
    print("____ ☁️ ______ ")

def main():
    """Main function to run the program.
    """

    for x in range(3):
        ad = fashion_ads()
        display_fashion_ads(ad)

