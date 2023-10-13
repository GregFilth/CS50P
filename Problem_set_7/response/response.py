from validator_collection import validators, errors


def main():
    email_address = input("What's your email address? ")
    print(validate(email_address))


def validate(e_addr):
    try:
        vail_email_address = validators.email(e_addr)
    except errors.EmptyValueError:
        return "Invalid"

    except errors.InvalidEmailError:
        return "Invalid"

    else:
        return "Valid"


if __name__ == "__main__":
    main()
