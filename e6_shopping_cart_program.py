foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q': # Q or q to quit
        break
    else:
        price = float(input(f"Enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price  # int + float = float

print("\n--- YOUR SHOPPING CART ---")

print()

for i in range(len(foods)):
    print(f"{foods[i]}:${prices[i]:.2f}")

print()

print(f"Total: ${total:.2f}")