# let's make a simple shopping cart program

print("---------------------------------------------------------------------")
print("                         Welcome to our shop                         ")
print("---------------------------------------------------------------------")

name = input ("What is your name:")
print (f"Welcome {name}")

print("                          choose your item                           ")

item = input("What item would you buy?:")
price = float(input("How much is it?:"))
quantity = int (input("How many would you buy?:"))
total_price = price * quantity
print()
print(f"HELLO {name}")
print(f"you have bought {quantity} of {item}s")
print(f"your total balance is: ${total_price}")

print("---------------------------------------------------------------------")
print("                             Good Bye                                ")
print("---------------------------------------------------------------------")