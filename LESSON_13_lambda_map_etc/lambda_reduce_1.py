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
        return orders__3[0][2] + calculate_total_revenue_2(orders__3[1:])

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