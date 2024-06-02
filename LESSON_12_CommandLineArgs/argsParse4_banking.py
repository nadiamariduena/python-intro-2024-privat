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
    #
    #
# 5 ENtry point of the program
if __name__ == "__main__":
    import argparse # Import the argparse module for commans-line argument parsing
    #
    #
    # 6 Create an argumentParser object with a description
    parser = argparse.ArgumentParser(
        description="Send money to another user."

    )
    #
    # 🟠 PARSER AMOUNT ----
    # 7 Add arguments for the amount to send, currency, and recipient's details
    parser.add_argument(
        "-a", "--amount", metavar="amount",
        type=float, required=True,
        help="The amount of money to send."
    )
    # 🟠 PARSER CURRENCY ----
    # 8
    parser.add_argument(
        "-c", "--currency", metavar="currency",
        required=True, choices=["USD", "EUR", "GBP" ],
        help="The currency of the amount to send."
    )

    # 🟠 PARSER RECIPIENT ----
    # 9
    parser.add_argument(
        "-r", "--recipient", metavar="recipient",
        required=True, nargs=2,
        help="The recipient's name and currency (e.g., 'John EUR)."

    )

#
#
    #10 parse the command line arguments
    args = parser.parse_args(

    )