import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2})(?:\:(\d{0,2}))? ([AP]M) to (\d{1,2})(?:\:(\d{0,2}))? ([AP]M)$", s):

        # fromH
        if int(matches.group(1)) < 12 and matches.group(3) == "AM":
            fromH = int(matches.group(1))
        if int(matches.group(1)) <12 and matches.group(3) == "PM":
            fromH = int(matches.group(1)) + 12
        if int(matches.group(1)) == 12 and matches.group(3) == "PM":
            fromH = int(matches.group(1))
        if int(matches.group(1)) == 12 and matches.group(3) == "AM":
            fromH = "0"
        if int(matches.group(1)) > 12:
            raise ValueError

        # fromM
        if matches.group(2) == None:
            fromM = "0"
        elif int(matches.group(2)) < 60:
            fromM = int(matches.group(2))
        elif int(matches.group(2)) >= 60:
            raise ValueError

        # toH
        if int(matches.group(4)) <12 and matches.group(6) == "AM":
            toH = int(matches.group(4))
        if int(matches.group(4)) <12 and matches.group(6) == "PM":
            toH = int(matches.group(4)) + 12
        if int(matches.group(4)) == 12 and matches.group(6) == "PM":
            toH = int(matches.group(4))
        if int(matches.group(4)) == 12 and matches.group(6) == "AM":
            toH = "0"
        if int(matches.group(4)) > 12:
            raise ValueError

        # toM
        if matches.group(5) == None:
            toM = "0"
        elif int(matches.group(5)) < 60:
            toM = int(matches.group(5))
        elif int(matches.group(5)) >= 60:
            raise ValueError

    else:
        raise ValueError

    return (f"{fromH:02}:{fromM:02} to {toH:02}:{toM:02}")

if __name__ == "__main__":
    main()