# Payment service
#---------------------------
from functools import reduce
#----------------------------
#
#
# ** pizza resto 2
# ------------
# include a payment service that accepts different types of cards to handle the total of the order. We'll define a dictionary mapping card types to their respective processing fees, and then we'll calculate the total revenue after deducting the processing fees.


#
def calculate_total_revenue_2(orders__3):

    if not orders__3: #Base case: If there are no order, return 0
        return 0
    else:
        # Extract the total price of the current order and add it to
        # the revenue
        #orders[0][2]: This part accesses the total price (the third element) of the first order in the orders list. Here's how it works:
        return orders__3[0][2] + calculate_total_revenue_2(orders__3[1:])
    #- calculate_total_revenue(orders[1:]): This part is a recursive call to the calculate_total_revenue function with a slice of the orders list, starting from the second order onwards. Here's what happens:
    #- orders[1:] creates a new list containing all orders except the first one.

    #
    # going down on the branch to reach the order[2]
# ** BY going down the branch i mean this: david is pos 0, pizza etc is pos 1, and 25 is position 2
# order[0]: Customer's name
# order[1]: Items ordered (a list of strings)
# order[2]: Total price of the order
    #


orders__3 = [
     ("Alice", ["Pizza", "Salad"], 25),
    ("Bob", ["Burger", "Fries", "Soda"], 20),
    ("Charlie", ["Pizza", "Wings", "Soda"], 30),
    ("David", ["Salad", "Soup"], 15),
    ("Eve", ["Pizza", "Burger", "Wings"], 35)
]




def process_payment(total_amount, card_type):
    #Define processing fees for different card types
    processing_fees = {
        "credit": 0.03, #3%
        "debit": 0.02, #2%
        "gift": 0.01,  # 1%
    }

    # Calculate the processing fee

    processing_fee = total_amount  * processing_fees.get(card_type, 0)

    # Deduct the processig fee from the total amount
    total_after_fee = total_amount - processing_fee

    return total_after_fee


total__revenue = calculate_total_revenue_2(orders__3)
print("Total revenue from orders (before processing fees):", total__revenue, "dollars")

# Process payment using a credit card
total__after_processing = process_payment(total__revenue, "credit")
print("Total revenue after processing fees (credit card):", total__after_processing, "dollars")

#

# Process payment using a debit card
total__after_processing = process_payment(total__revenue, "debit")
print("Total revenue after processing fees (debit card):", total__after_processing, "dollars")

# Process payment using a gift card
total__after_processing = process_payment(total__revenue, "gift")
print("Total revenue after processing fees (gift card):", total__after_processing, "dollars")

# result

# Total revenue from orders (before processing fees): 125 dollars
# Total revenue after processing fees (credit card): 121.25 dollars
# Total revenue after processing fees (debit card): 122.5 dollars
# Total revenue after processing fees (gift card): 123.75 dollars