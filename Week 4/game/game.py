#I’m thinking of a number between 1 and 100, what is it?
# import randint from random to provide random number
from random import randint

# ask user for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# create a random number
random_numb = randint(1, level)

# ask for guess and then check if same as random number
while True:
    try:
        # make sure guess is greater than 0
        guess = int(input("Guess: "))
        if guess > 0:
            # if guess is less than random number
            if guess < random_numb:
                print("Too small!")
            # if guess is larger than random number
            elif guess > random_numb:
                print("Too large!")
            # if guess is correct
            else:
                print("Just right!")
                break
# if guess isn't an integer then ask again
    except:
        pass
