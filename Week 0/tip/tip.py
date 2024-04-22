# Calculate the tip including stripping out $ signs then adding back in at end and calculating % tip

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Strip out $ signs if used. Make input into a decimal
def dollars_to_float(d):
    d = d.strip("$")
    d = float(d)
    return d

# strip out % signs if used. Calculate percentage according to percent
def percent_to_float(p):
    p = p.strip("%")
    p = float(p) / 100
    return p


main()
