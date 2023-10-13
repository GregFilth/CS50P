
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    A = is_alphabetic(s)
    B = length(s)
    C = nums_in_mid(s)
    return (A and B and C)


def is_alphabetic(s):
    return s[:2].isalpha()


def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def nums_in_mid(s):
    if s.isalpha():
        return True
    elif s.isalnum():
        for i in range(len(s)):
            if s[i].isnumeric():
                if s[i] != "0":
                    return (s[i:].isnumeric())
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()
