from pyfiglet import Figlet
from random import choice
import sys

# Set figlet
# get all the fonts
figlet = Figlet()
figlet.getFonts()

# Get list of fonts and apply to user choice
f = choice(figlet.getFonts())

# Check how many command prompt arguments there are
# If just one (i.e. no font chosen) then True (so random font will be used)
# If 3 arguments AND 1st argument is -f then assume a font so False
# If nothing entered then return error message and exit
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)


# if a font has been chosen then check font list for that font.
# if not in that font list then return erorr message and exit
# else set the chosen font
if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = choice(figlet.getFonts())

# set the output variable
# print the output message text
# render in chosen font
output = input("Input: ")
print("Output: ")
print(figlet.renderText(output))
