from emoji import emojize

# Get a text emoji from the user, convert it to emoji symbol and return their message and emoji symbol

# ask user for message
user_string = input("Input: ").strip()

# print message with emoji symbol
print("Output: ", emojize(user_string, language="alias"))
