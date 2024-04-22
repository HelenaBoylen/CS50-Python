import requests
from datetime import datetime
import sys

# Note: that after completing this code I discovered that there is an existing wrapper that would do this! - ISS-Info
# -------------------------------

# Declare the first name so I can re-use it as a global
first_name = ""

# -------------------------------


# Ask the user's name. Bins the last name if given, backs off slowly if no name given...
def main():
    global first_name
    full_name = input("Enter your name: ")
    names = full_name.split()
    if names:
        first_name = names[0]
        print("Hi", first_name, "let's get started!")
    else:
        print("Okay, let's get started!")
    iss_info()


# -------------------------------


# Assemble the sorted crew names, lat and long - then print them with a link to googlemaps for ISS current positon
def iss_info():
    crew = current_crew()
    sorted_names = sort_by_last_name(crew)
    latitude, longitude = current_location()
    days_occupied = occupied_since()
    ascii_art = display_ascii_art()
    print("\n+---------------------------------+")
    print("| THE INTERNATIONAL SPACE STATION |")
    print("+---------------------------------+")
    if first_name != "":
        print("\n** Hi,", first_name, "Welcome to the ISS **")
    print("\nCurrent crew on the ISS:")
    print("------------------------\n")
    for name in sorted_names:
        print("*", name)
    print("\nCurrent ISS position:")
    print("---------------------\n")
    print("Latitude:", latitude)
    print("Longitude:", longitude, "\n")
    print(
        "Google Map Link: https://www.google.com/maps/search/?api=1&query="
        + latitude
        + ","
        + longitude
        + "&zoom=1"
    )
    print("\nA bit of History")
    print("----------------\n")
    with open("history.txt", "r") as file:
        history_content = file.read()
    print(history_content)
    print(
        "As of today's date, ISS has been occupied for approximately",
        days_occupied,
        "days.\n\n",
    )
    print(ascii_art)


# -------------------------------


# Get the list of current ISS crew from open-notify.org, return the names of each crewmember
def current_crew():
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        crew = response.json()["people"]
        return [person["name"] for person in crew]
    except requests.RequestException:
        print("ISS Crew info currently unavailable")
        return []


# -------------------------------


# Sort astronaut names by last name then return them
def sort_by_last_name(names):
    sorted_names = sorted(names, key=get_last_name)
    return sorted_names


# -------------------------------


# Split the name into first and last names and return the last name to enable proper sorting
def get_last_name(name):
    split_name = name.split()
    return split_name[-1]


# -------------------------------


# Get the current location of the ISS from open-notify.org, return lat and long from the iss_position dict.
def current_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        iss_position = data["iss_position"]
        latitude = iss_position["latitude"]
        longitude = iss_position["longitude"]
        return latitude, longitude
    except requests.RequestException:
        print("ISS location info currently unavailable")
        return []


# -------------------------------


# Calculate days occupied since first astronauts arrived on ISS. Use dateime library
def occupied_since():
    start_date = datetime(2000, 11, 2)
    today = datetime.now()
    days_since_occupied = (today - start_date).days
    return days_since_occupied


# -------------------------------


# Read contents of iss.txt
def display_ascii_art():
    with open("iss.txt", "r") as file:
        ascii_art = file.read()
    return ascii_art


# -------------------------------

# Do it!
if __name__ == "__main__":
    main()
