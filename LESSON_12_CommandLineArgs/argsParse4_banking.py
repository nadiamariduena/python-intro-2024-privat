# 1
def send_money(amount, currency, recipient):
    #define exchange rates between currencies using a nested dictionary
    exchange_rates = {
        #GBP) is the currency of the United Kingdom
        "USD": {"EUR": 0.82, "GBP": 0.72},  # Exchange rates from USD to EUR and GBP
        "EUR": {"USD": 1.22, "GBP": 0.88}, # Exchange rates from EUR to USD and GBP
        "GBP": {"USD": 1.39, "EUR": 1.14} # Exchange rates from GBP to USD and EUR

    }

    # 2 Check if the specified currency or the recipient's currency is not supported
    if currency not in exchange_rates or recipient["currency"] not in exchange_rates[currency]:
        print("Sorry, we dont support this currency exchange.")
        # cut the process if not
        return

    # 3 Calculate the converted amount based on the exchange rates
    converted_amount = amount * exchange_rates[currency][recipient['currency']]

    # 4 Print a message indicationg the amount sent and the recipient's details
    print(f"Sending {converted_amount:.2f} {recipient['currency']} to {recipient['name']}")
    #
    #
    #----
# ENtry point of the program
if __name__ == "__main__":
    import argparse # Import the argparse module for commans-line argument parsing
