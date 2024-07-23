import random

class Ad:
    def __init__(self, ad_id, ad_type, content, image_url=None):
        self.ad_id = ad_id
        self.ad_type = ad_type
        self.content = content
        self.image_url = image_url

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