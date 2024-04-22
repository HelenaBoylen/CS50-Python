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
# check_punctuation checks for punctuation marks
# no_nums_first_half(plate) checks routine below is true
# first_digit(plate) != '0' returns first digit in string and checks it's not zero
# returns TRUE if all the above are true and triggers print("Valid") or print("Invalid")

def is_valid(plate):
    if len(plate) <7 and len(plate) > 1 and plate[0:2].isalpha() and plate.isalnum and no_nums_first_half(plate) and check_punctuation(plate) == True and first_digit(plate) != '0':
        return True
    else:
        return False

# checks for numbers appearing in first half of string
def no_nums_first_half(plate):
    half = len(plate) // 2
    first_half = plate[:half]
    return not any(char.isdigit() for char in first_half)

# checks for zeros being first digit in string
def first_digit(plate):
    for char in plate:
        if char.isdigit():
            return char
    return None

# checks for punctuation
def check_punctuation(plate):
    for char in plate:
        if char in [",",".","!","?",";"]:
            return False

if __name__ == "__main__":
    main()

