#dictio 1
member1 = {
    'name': 'Robert Plant',
    'instrument': 'vocals'
}
#---------
#dictio 2
member2 = {
    'name': 'Jimmy Page',
    'instrument': 'guitar'
}
#---------
#dictio 3
# here we will nest the 2 dictios from above
band = {
    "member1": member1,
    "member2": member2
}
#
# show the content
print(band)
# result
# {'member1': {'name': 'Robert Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Jimmy Page', 'instrument': 'guitar'}}

#
#
#---------
print('----------')

ecommerce_shop = {
# ✋ Each top-level key represents a product category (e.g., "electronics", "clothing").

    "electronics": {
        "phones": [
           # ✋ Each category key maps to a dictionary where keys are subcategories (e.g., "phones", "laptops" under "electronics").
           #
            {"name": "iPhone 13", "price": 999},
            {"name": "Samsung Galaxy S21", "price": 899},
            {"name": "Google Pixel 6", "price": 699}
        ],
        "laptops": [
            {"name": "MacBook Pro", "price": 1499},
            {"name": "Dell XPS 15", "price": 1299},
            {"name": "HP Spectre x360", "price": 1199}
        ]
    },
    "clothing": {

        "men": [
            {"name": "T-shirt", "price": 20},
            {"name": "Jeans", "price": 50},
            {"name": "Jacket", "price": 80}
        ],
        "women": [
            {"name": "Dress", "price": 60},
            {"name": "Skirt", "price": 40},
            {"name": "Blouse",

            # ✋ Each subcategory key maps to a list of dictionaries, each representing a product with keys "name" and "price".
            "price": 30}
        ]
    }
}

# --- iterate on the data

# Get the laptops available in the electronics category
laptops = ecommerce_shop["electronics"]["laptops"]
for laptop in laptops:
    print(laptop["name"], "-", laptop["price"])
# Output:
# MacBook Pro - 1499
# Dell XPS 15 - 1299
# HP Spectre x360 - 1199
