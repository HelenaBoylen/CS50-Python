# output calories per portion of fruit entered by user
# asks the user to input a fruit, strips out whitespace and converts to lowercase
choice = input("Item: ").strip().lower()

# Dict of fruit and calories. Note numbers have no ""s Also this doesn't work if fruit capitalised
fruit = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 60,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# outputs calories for chosen fruit
if choice in fruit:
      print("Calories:", (fruit[choice]))

