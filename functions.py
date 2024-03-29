 #Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
 #The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
 
def calculate_discount(price, discount_percent):
    
#If the discount is 20% or higher, apply the discount; otherwise, return the original price.

    if discount_percent >=20:
        discount_amount = price * (discount_percentage/100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

#Print the final price after applying the discount, or if no discount was applied, print the original price

final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print("The original price is: Ksh {:.2f}".format(original_price))
else:
    print("The final price after discount is: Ksh {:.2f}".format (final_price))
