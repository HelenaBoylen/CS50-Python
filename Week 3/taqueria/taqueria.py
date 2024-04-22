# Prompt user for menu item, then keep running total. When user hits Ctrl D, make a total
# Write the menu dict
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Zero the bill variable

total_bill = 0

# while loop to ask for menu item, check it's in the menu and add it to the bill or ask again if item not on menu

while True:
    try:
        item = input("Item: ").title().strip()
        if item in menu:
            total_bill += menu[item]
            print(f"Total: ${total_bill:.2f}")

# Error message about items not on menu - but fails check50 so removed
       # else:
         # print("That item does not exist")

# error handling.
    except EOFError:
        print("\n")
        quit()

