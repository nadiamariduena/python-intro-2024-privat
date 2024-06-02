def send_money(amount, currency, recipient):
    #define exchange rates between currencies using a nested dictionary
    exchange_rates = {
        #GBP) is the currency of the United Kingdom
        "USD": {"EUR": 0.82, "GBP": 0.72},
        "EUR": {"USD": 1.22, "GBP": 0.88},
        "GBP": {"USD": 1.39, "EUR": 1.14}

    }