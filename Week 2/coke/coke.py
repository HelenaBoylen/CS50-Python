# Prompt user for coins. Inform user of amount remaining then inform of change if any
# set the initial value
cost = 50

# Say amount outstanding and ask for a coin
while cost > 0:
    print("Amount Due:", cost)
    coins = int(input("Insert Coin: "))

# check coin is in the list of acceptable coins
    if coins in [5, 10, 25]:

# If acceptable coin then take that amount away from outstanding amount
        cost -= coins

# Calculate if change owed by working out absolute amount still owed
change_owed = abs(cost)

# Print amount of changed owed.
print("Change Owed:", change_owed)
