# Prompt user for vanity plate then check output valid.
# - First 2 chars must be letters
# - Between 2-6 chars
# - Numbers must come at end
# - No periods, spaces of punctuation marks

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# checks validity and returns true if valid
# if len(plate) <7 checks string less than 7 chars
# len(plate) > 1 checks string longer than 1 char
# plate[:2].isalpha() checks first two chars are alphas
# no_nums_first_half(plate) checks routine below is true
# first_digit(plate) != '0' returns first digit in string and checks it's not zero
# returns TRUE if all the above are true and triggers print("Valid") or print("Invalid")

def is_valid(s):
    if len(s) <7 and len(s) > 1 and s[:2].isalpha() and no_nums_first_half(s) and first_digit(s) != '0':
        return True
    else:
        return False

# checks for numbers appearing in first half of string
def no_nums_first_half(s):
    half = len(s) // 2
    first_half = s[:half]
    return not any(char.isdigit() for char in first_half)

# checks for zeros being first digit in string
def first_digit(s):
    for char in s:
        if char.isdigit():
            return char
    return None

main()

# Note probably better to use "s" than "plate" e.g. len(s) not len(plate), but for now this is easier for me to track

