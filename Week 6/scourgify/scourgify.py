# Tidy up a .csv file including split comma-separated value into 2 fields
import sys
import csv

def main():
    check_args()
    directory = []

    try:
        # open and read the csv file
        with open(sys.argv[1], "r")as new_csv:
            # create a variable to hold the info so we can do stuff to it
            temp_csv = csv.DictReader(new_csv)

            # split data in name col by "," then add to variable with 3 headers
            for row in temp_csv:
                split_name = row["name"].split(",")
                directory.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"] })

    # Error message
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


    # open second file and write data to it
    with open(sys.argv[2], "w")as new_file:
            fieldnames=["first", "last", "house"]
            write_file = csv.DictWriter(new_file, fieldnames)

            # create new headers
            write_file.writeheader()
            for row in directory:
                write_file.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

# check the sys.argvs
def check_args():
    # check length of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check whether .csv file
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV File")

if __name__ == "__main__":
    main()
