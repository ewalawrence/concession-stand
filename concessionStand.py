# Concession Stand

menu = {
    "popcorn" : 2.40,
    "chocolate" : 5.50,
    "yoghurt" : 12.40,
    "coke": 23.40
    }
cart = []
total = 0

print("----------Menu-----------")
for key, value in menu.items():
    print(f"{key.title():20} : ${value:.2f}")
print()

while True:
    food = input('Select your choice (q to quit): ').lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not found in the menu. Please try again.")

print()
print("----------Your Orders-----------")
for food in cart:
    total += menu.get(food)
    print(food.title(), end=" ")  # Print the items in title case for display


total += menu.get(food)
print(f"\n\nTotal: ${total:.2f}")
