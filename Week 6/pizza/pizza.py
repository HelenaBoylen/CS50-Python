# Get a .csv filename from sys.argv then output ASCII art table of contents
import csv
import sys
from tabulate import tabulate

def main():
    check_args()
    # initialise the list
    menu = []
    try:
        # open and read the csv file
        with open(sys.argv[1], "r")as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)
        # print the csv file in table format
        print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))
    # error message if can't find file
    except FileNotFoundError:
        sys.exit("File does not exist")

# check the sys.argvs
def check_args():
    # check length of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check whether .csv file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV File")

if __name__ == "__main__":
    main()
