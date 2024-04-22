# Create a list to keep a running total of items and numbers of items.
# Initiate shopping list

shopping_list = {}

# Create a while loop

while True:
    try:
        # Prompt user for item and convert to uppercase
        item = input().upper()

        # if item is already in the dict, add 1

        if item in shopping_list:
            shopping_list[item] += 1

        # if item isn't in the dict, add it to the dict

        else:
            shopping_list[item] = 1

# when the user types Ctrl d, print a list of items in shopping_list in alphabetical order with number of items

    except EOFError:
        for item in sorted(shopping_list):
            print(shopping_list[item], item)
        break
