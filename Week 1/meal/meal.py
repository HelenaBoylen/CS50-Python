# Check the time and respond with correct meal name.

def main():
    reply = input("What's the time? ")
    time = convert(reply)

# check time greater than or less than certain times
# just to see if it worked I used < and > with x.59 and x.01
# but that's an extra 4 characters per line, so don't do that!

    if time > 6.59 and time < 8.01:
        print("breakfast time")

    elif time > 11.59 and time < 13.01:
        print("lunch time")

    elif time > 17.59 and time < 19.01:
        print("dinner time")

# split the str into "xx" : "xx" then make them floats.
def convert(time):
    h, m = time.split(":")
    mins = float(m) / 60
    return float(h) + mins

# honestly not sure what this does, but make sure it has all "_"s and "main()" indented or will fail
if __name__ == "__main__":
    main()
