# Users should specify how many bitcoins they want to buy in command line arg. Check for float. output value of bitcoin to 4 dec.
import sys
import requests


# Convert user's int to a float.
try:
    if len(sys.argv) == 2:
        amount = float(sys.argv[1])
        try:
            # Check the current bitcoin rate and calculate total
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin = response.json()["bpi"]["USD"]["rate_float"]
            total = float(bitcoin) * amount
            print(f"${total:,.4f}")

        # If there was a problem with the conversion process
        except requests.RequestException:
            print("ERROR")
            sys.exit(1)

    # If they didn't enter anything
    else:
        sys.exit("Missing command-line argument")

# If they entered something that isn't a number
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
