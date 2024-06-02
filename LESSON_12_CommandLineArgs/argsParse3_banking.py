def send_money(amount, currency, recipient):
    #define exchange rates between currencies using a nested dictionary
    exchange_rates = {
        #GBP) is the currency of the United Kingdom
        "USD": {"EUR": 0.82, "GBP": 0.72},

    }