item = input("What item woule you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bougth {quantity} x {item}/s")
print(f"You total is: {round(total, 2)}$")