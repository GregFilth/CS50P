import sys



def main():
    count = 0
    if len(sys.argv) == 2:
        if sys.argv[1].strip().endswith(".py"):
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        if line != "\n" and line.strip() != "" and not line.lstrip().startswith("#"):
                            count += 1

            except FileNotFoundError:
                sys.exit("File does not exist")
            else:
                print(count)

        else:
            sys.exit("Not a Python file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
