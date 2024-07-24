import random

def fashion_ads():

    the_ads = [
        {"image": "image1.jpg", "text": "Discover our Summer Collection!"},
        {"image": "image2.jpg", "text": "Explore the Latest Trends in Fashion!"},
        {"image": "image3.jpg", "text": "Get Ready for Fall with Our New Arrivals!"},
        {"image": "image4.jpg", "text": "Stay Stylish This Winter Season!"}


    ]


    return random.choice(the_ads)