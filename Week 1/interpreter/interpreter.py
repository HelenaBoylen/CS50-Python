# Ask for an expression and calculate output

expression = input("Expression: ").strip()

# Break expression into 3 bits
x, y, z = expression.split(" ")

# Make first and last bits floats
first_number = float(x)
second_number = float(z)

# Do the maths
if y == "+":
    answer = first_number + second_number
if y == "-":
    answer = first_number - second_number
if y == "*":
    answer = first_number * second_number
if y == "/":
    answer = first_number / second_number

# Print the answer
print(answer)
