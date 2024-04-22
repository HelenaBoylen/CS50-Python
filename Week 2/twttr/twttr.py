# Prompt user for some text then return the text without vowels

# Ask for input
def main():
      phrase = input("Input: ")
      output = ""

# check the letters in the input phrase for vowels iterating through with a for loop
      for letters in phrase:
            if vowels(letters):
# concantenate the letters back together
                  output += letters
# print the output
      print("Output:", output)

# define the vowels list
def vowels(n):
      if n not in "aeiouAEIOU":
            return True

main()
