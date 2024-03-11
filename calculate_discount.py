# Week 3 - Assignment.
# Create a function calculate_discount(price, discount_percent) that calculates the final
# price after applying a discount. If discount is 20% or higher, apply the discount, otherwise return original_price.
# prompt user for inputs e.g. price & discount.


price = int(input("\n Enter item Price : "))
discount = int(input(" Enter item discount : "))

def calculate_discount(price, discount_percent):
    if discount >= 20:
        price = price - (price * (discount/100))
        return price
    else:
        return price
    
print(" discounted price : ",calculate_discount(price, discount))