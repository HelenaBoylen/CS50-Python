# Ask for level, then generate 10 maths questions and scrore user at end. Return EEE for non ints.
from random import randint

def main():
    level = get_level()
    score = questions(level)
    print("Score: ", score)

# Ask user for level 1, 2 or 3. If incorrect answer, repeat.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                 break
        except:
            pass
    return level

# Create 2 variables for addition depending on level 1, 2 or 3 using random.randint
def generate_integer(level):
    if level == 1:
            x = randint(0, 9)
            y = randint(0, 9)
    elif level == 2:
            x = randint(10, 99)
            y = randint(10, 99)
    else:
            x = randint(100, 999)
            y = randint(100, 999)
    return x,y

# Check user attempts and if answer correct. If not return EEE and add 1 to attempts up to 3
def attempts (x, y):
    count_attempts = 1
    while count_attempts <= 3:
         try:
              answer = int(input(f"{x} + {y} = "))
              if answer == (x + y) :
                   return True
              else:
                   count_attempts += 1
                   print("EEE")
         except ValueError:
              print("EEE")
              count_attempts += 1
    print(f"{x} + {y} = {x+y}")
    return False

# Keep track of user correct answers until question count reaches 10. Return score.
def questions(level):
     q_count = 1
     score = 0
     while q_count <= 10:
          x, y = generate_integer(level)
          response = attempts(x,y)
          if response == True:
               score += 1
          q_count += 1
     return score

if __name__ == "__main__":
    main()

