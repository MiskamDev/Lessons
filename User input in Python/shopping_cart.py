item = input("What item would you like to buy?: ")  # User input for item
price = float(input("What is the price?: "))        # User input for price
quantity = int(input("How many would you like?: ")) # User input for quantity

total = price * quantity  # Calculating total cost

print(f"You have bought {quantity} x {item}/s") # Displaying the item and quantity
print(f"Price per item: {price}$")              # Displaying the price per item
print(f"Your total is: {round(total, 2)}$")     # Displaying the total cost