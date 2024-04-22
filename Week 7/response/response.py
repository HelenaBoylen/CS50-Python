# Ask for user's email address, check valid against Validator library, return Valid or Invalid
import validators


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(user_email):
    if validators.email(user_email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

