import inflect
p = inflect.engine()

# initialise the empty list to contain the names
input_names = []

# loop through asking for names until user hits Ctrl+D
while True:
    try:

# Ask user for input
        name = input("Name: ")
        input_names.append(name)

# print a new line and break out when user hits Ctrl+D
    except EOFError:
        print()
        break

# create variable to join words in a list with comma separator and "and" as final separator
names = p.join(input_names)

# print "Adieu, adieu to" plus the contents of output variable
print("Adieu, adieu, to " + names)

