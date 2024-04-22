# Take a string for 12hr time format and convert to 24hr checking format and time entered appropriately
import re
import sys


def main():
    print(convert(input("Hours: ")))

# RegEx to pattern match input times and assign to variable
# check hr bits are > 12 else ValueError
# use format_24 function to assemble new time
def convert(s):
    time_input = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if time_input:
        time_bits = time_input.groups()
        if int(time_bits[1]) > 12 or int(time_bits[5]) > 12:
            raise ValueError
        from_time_bits = format_24(time_bits[1], time_bits[2], time_bits[3])
        to_time_bits = format_24(time_bits[5], time_bits[6], time_bits[7])
        return from_time_bits + " to " + to_time_bits
    else:
        raise ValueError

# function to check if pm and hr is 12, then keep that else add 12. If am and hr = 12 then 00
# if mins are missing then add 00
# if mins > 59 or hr > 12 then ValueError
def format_24(old_hour, old_minute, am_pm):
    if am_pm == "PM":
        if int(old_hour) == 12:
            new_hour = 12
        else:
            new_hour = int(old_hour) + 12
    else:
        if int(old_hour) == 12:
            new_hour = 0
        else:
            new_hour = int(old_hour)
    if old_minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    elif int(old_minute) > 59:
        raise ValueError
    elif int(old_hour) > 12:
        raise ValueError
    else:
        new_time = f"{new_hour:02}" + ":" + old_minute
    return new_time



if __name__ == "__main__":
    main()
