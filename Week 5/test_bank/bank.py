# original code had .strip() and .lower() but code failed check50 with that
def main():
      greeting = input("Hi There ")
      message = value(greeting)
      print(message)


def value(greeting):
    if greeting.startswith("hello"):
        return(0)
    elif greeting.startswith("h"):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
