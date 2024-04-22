# convert camelCase filename to snake_case

answer = input("camelCase? ")

# make a list
camel_case = []
# check if letters are upper or lowercase
for letters in answer:
# if uppercase, add an underscore and make lowercase
    if letters.isupper():
        letters = "_" + letters.lower()
# add them to the previous lowercase letters
    camel_case.append(letters)
# print it out
print("".join(camel_case))


# This seems easier though
# answer = input("camelCase: ")
# camel_case = ""
#
# for char in answer:
#     if char.isupper():
#         camel_case += '_' + char.lower()
#     else:
#         camel_case += char
# print("snake_case:", camel_case)

