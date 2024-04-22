# Convert inputted dates to ISO 8601 format

# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Create a loop
while True:

    # Ask the user for the date
    user_date = input("Date: ").title().strip()

    # split the string into 3 using / as delimiter. Check months less than 12 and days less than 31
    try:
       month, day, year = user_date.split("/")
       if(int(month) <= 12) and (int(day) <= 31):
           break

    # if that's not right then:
    except:
        try:

             # check if comma in string, if so do this
             if "," in user_date:

                # split the string with space as the delimeter
                long_month, long_day, year = user_date.split(" ")

                # find the position in the list of the month variable by counting list items
                for m in range(len(months)):
                    if long_month in months:

                        # add 1 to the list position number to account for list starting at 0
                        month = months.index(long_month)+1

                # remove the comma
                day = long_day.replace(",", "")

                # check months var less than 12 and day var less than 31
                if(int(month) <= 12) and (int(day) <= 31):
                    break

        #If that's not right then:
        except:

            # print new line
            print("\n")

            # do it again
            pass

# print the date with added zeros for single digits.
print(f"{year}-{int(month):02}-{int(day):02}")

quit()
