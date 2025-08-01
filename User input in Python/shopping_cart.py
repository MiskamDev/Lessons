# User Input and Arithmetic Operations
# This script collects user input for name, age, item, price, and quantity,
# then calculates the total cost of the items purchased.
name = input("Enter your name: ") # Get user name
age = int(input("Enter your age: ")) # Get userы age

item = input("Enter the item you want to buy: ") # Get item name
price = float(input("Enter the price of the item: ")) # Get item price
quantity = int(input("Enter the quantity you want to buy: ")) # Get item quantity

total_cost = price * quantity # Calculate total cost

print(f"\nHello {name}, you are {age} years old.") # Display user info
print(f"You have purchased {quantity} {item}(s) at a price of ${price:.2f} each.")
print(f"The total cost of your purchase is: ${total_cost:.2f}") # Display total cost
print("Thank you for your purchase!") # Thank the user