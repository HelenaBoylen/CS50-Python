# International Space Station Realtime Data

#### Video Demo:  [International Space Station - Realtime Data](https://youtu.be/0cDqegzj3XI)

#### Description:
This programme produces realtime data about the International Space Station (ISS) including:
1. Current Crew on board
2. Current location
3. Link to current position on Googlemaps
4. Some brief history about the station
5. A calculation of how many days the station has been occupied
6. Some ASCii art

The general idea is to have a little programme that the user might bookmark and return to frequently.

## Functions Used:


**Main**: Asks you your name and then says "Hi" (your name). If the user types in two or more names, the function only stores and repeats their first name. If the user just returns and doesn't answer the question - no problem, perhaps they're the private type - the programme says "Okay, Let's get started!" and the second function is called.

**ISS Info**: This assembles all the data produced by the following functions and prints it to the screen. If the user has given a name, then their name (first name only if two are given) is printed with a "Welcome" message underneath the main heading. As well as printing results from the following functions, this function also constructs a link to a Google Map page with the current position of the ISS taken from the Current Location function. This function also includes the contents of a .txt file with a brief history of the ISS including when it was first inhabited and the initial build date.

**Current Crew**: This calls the opennotify.org ISS crew API which lists the current crew members of the ISS. If for some reason the API is unavailable, it prints a message saying the Crew Member data is unavailable. This list of crew members is not sorted in any way.

**Get Last Name**: As the list of crew members as taken from the opennotify.org API is not sorted, this function splits the crew member's name into first and last chunks to enable sorting by last name.

**Sort by Last Name**: This function takes the result of the previous Get Last Name function and then sorts the list of names by last name before finally re-assembling them. This is then collected by the ISS Info function which displays the list in last name order with an added asterisk in lieu of a bullet.

**Current Location**: This function calls the opennotify.ore ISS location API to print out the current Latitude and Longitude of the ISS in decimal format. If the API is unavailable for some reason, it returns and error message saying it's unavailable.

**Occupied Since**: This function sits at the end of a line of text and it calculates the number of days that the ISS has been permanently inhabited since the first crew arrived on 2nd November 2000. This is then printed out by the ISS Info function.

**Display ASCii Art**: This function includes a little ASCii representation of the ISS which I produced myself (can you tell?) which lives in a .txt file and is included at the bottom of the terminal page by the ISS Info function.


```
 # # # #             # # # #
 # # # #  ___::___   # # # #
 # # # #   | [] |    # # # #
 # # # #   | [] |    # # # #
 ---------<------>----------
 # # # #   | [] |    # # # #
 # # # #   | [] |    # # # #
 # # # #  ---::---   # # # #
 # # # #     ++      # # # #
```
```
