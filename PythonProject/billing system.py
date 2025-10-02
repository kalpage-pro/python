# simple billing system for bakery called BunTalk

print("-------------------------------------------")
print("           Welcome to BunTalk"              )
print("-------------------------------------------")

print("""
    A) Muffin
    B) Bread
    C) Croissant
    D) Role
    E) Pizza
    F) Burger

""")

item = input("Select your item character: ")
quantity = float(input("Enter your Quantity: "))

if item == "A":
    value = 15.00 *quantity
    print(f"total: {round(value, 2)}")
elif item == "B":
    value = 20.00 * quantity
    print(f"total: {round(value, 2)}")
elif item == "C":
    value = 12.70 * quantity
    print(f"total: {round(value, 2)}")
elif item == "D":
    value = 10.05 * quantity
    print(f"total: {round(value, 2)}")
elif item == "E":
    value = 22.50 * quantity
    print(f"total: {round(value, 2)}")
elif item == "F":
    value = 30.25 * quantity
    print(f"total: {round(value, 2)}")
else:
    print(f"{item} is in not our order list")

print("-------------------------------------------")
print("                 Come Again                ")
print("-------------------------------------------")