# Return lines of code in a python file from sys.argv checking for comments, empty lines
# Exit if too many or too few arguments or if not a python file
import sys

def main():
    # check command line arguments
    check_argvs()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    # initialise the line count
    line_count = 0
    # add to the count if lines aren't empty or comments
    for line in lines:
        if check_empty_or_comment(line) == False:
            line_count += 1
    # print the number of lines
    print(line_count)


# Function to check command line args contain a python file name
def check_argvs():
    # check length of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    # check whether python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python File")

# Function to check if lines are empty or comments
def check_empty_or_comment(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
