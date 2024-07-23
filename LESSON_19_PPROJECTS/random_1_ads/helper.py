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