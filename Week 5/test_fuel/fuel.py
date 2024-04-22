# Prompt user for fraction. Convert fraction to %. Return % unless 1% then return E or 99% then return F
def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))

# convert fraction into percentage
# have to use top/bottom instead of x/y or I get confused!
def convert(fuel):
        top, bottom = fuel.split("/")
        top = int(top)
        bottom = int(bottom)
        percentage = round(100 * (top / bottom))
        return(percentage)

# calculate percentage
def gauge(percentage):
    if percentage <= 1:
        percentage = 'E'
    elif percentage >= 99:
        percentage = 'F'
    if str(percentage).isnumeric():
        percentage = str(percentage) + '%'
    return(percentage)

if __name__ == '__main__':
    main()
