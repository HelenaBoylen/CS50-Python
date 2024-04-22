# validate an IP address
import re

def main():
    print(validate(input("IPv4 Address: ")))

# check each chunk of IP is a number between 0-9.
def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        # check each number is less than or equal to 255
        if int(matches.group(1)) <= 255 and int(matches.group(2)) <= 255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <= 255:
           return True
    return False


if __name__ == "__main__":
    main()


