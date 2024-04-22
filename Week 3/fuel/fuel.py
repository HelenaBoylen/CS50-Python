# Prompt user for fraction. Convert fraction to %. Return % unless 1% then return E or 99% then return F
# start a while loop
while True:
    # ask for input
    fuel = input("Fraction: ")
    try:
        # split the fraction into top and bottom figures
        top, bottom = fuel.split("/")
        #create 2 new variables with these figures
        new_top = int(top)
        new_bottom = int(bottom)
        # create new variable which equals top figure divided by bottom figure
        f = new_top / new_bottom
        # if this is less than 1 then break
        if f <= 1:
            break
    # if error on input ask again with no error message
    except (ValueError, ZeroDivisionError):
        pass
# create new variable tank which is the f variable x 100 rounded.
tank = round(f * 100)
# if tank is less than or equal to 1 return E
if tank <= 1:
    print("E")
# if tank is greater than or equal to 99 return F
elif tank >= 99:
    print("F")
# else return %
else:
    print(f"{tank}%")
    # can't use print(tank,"%") as adds a space before %


