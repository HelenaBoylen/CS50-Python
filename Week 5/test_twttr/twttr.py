# Prompt user for some text then return the text without vowels
# Ask for input
def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    no_vowels = ""
    for letters in word:
        if letters not in ["a", "e", "i" ,"o" ,"u" , "A", "E", "I", "O", "U"]:
            no_vowels += letters
    return("".join(no_vowels))

if __name__ == "__main__":
    main()
