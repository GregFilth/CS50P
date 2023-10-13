import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # search for (num).(num).(num).(num)
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):

        # if all numbers are lower than 256 and first number is higher than 0
        if 0 < int(matches.group(1)) < 256 and int(matches.group(2)) < 256 and int(matches.group(3)) < 256 and int(matches.group(4)) < 256:
            return True
        else:
            return False

    else:
        return False

if __name__ == "__main__":
    main()
