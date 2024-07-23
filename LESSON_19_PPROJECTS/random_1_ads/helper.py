import random

class Ad:
    # STEP 1, declare the PARAMETERS: ad_id, ad_type, content, image_url=None / ad_id, ad_type, content, and image_url=None are parameters of the __init__ method of a class.

    # INIT method: This is a special method in Python classes that is automatically called when a new instance of the class is created. It initializes (sets up) the initial state of the object by assigning values to its attributes
    def __init__(self, ad_id, ad_type, content, image_url=None):
        #image_url=None specifies that image_url is an optional parameter. If no value is provided for image_url when creating an object, it defaults to None
        self.ad_id = ad_id
        self.ad_type = ad_type
        self.content = content
        self.image_url = image_url
        #


#👾 This will display on your terminal the properties from STEP 1.
    def display(self):
        print(f"DISPLAYING {self.ad_type} AD #{self.ad_id}:")
        print(f"CONTENT: {self.content}")
        #
        # IMG
        # if there is img then show it
        if self.image_url:
            print(f"IMAGE url: {self.image_url}")

        print("_____ 🌻 _____")


# List of ads
ads_pool = [
    Ad(1,
       "Banner",
       "Get 20% off on premium subscription",
        "https://example.com/banner1.jpg"),
    Ad(2, 'Sponsored Post', 'Discover the latest trends in fashion.', 'https://example.com/post1.jpg'),
    Ad(3, 'Video Ad', 'Watch our new product in action.', 'https://example.com/video1.jpg'),
]

# Function to randomly select and return and ad

def get_random_ad():
  return random.choice(ads_pool)
#random.choice is a function from the random module in Python that allows you to randomly select an element from a non-empty sequence, such as a list, tuple, or string. Here's what it means and how it works