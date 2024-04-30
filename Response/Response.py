import validator_collection


def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(s):
    if validator_collection.checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
