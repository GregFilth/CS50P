import sys
import csv
from tabulate import tabulate


def main():
    pizzas = []
    i = 0

    if len(sys.argv) == 2:
        if sys.argv[1].strip().endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if i == 0:
                            row0 = row
                            x, y, z = (
                                str(list(row0))
                                .replace("[", "")
                                .replace("]", "")
                                .replace("'", "")
                            ).split(", ")
                            i = 1
                        pizzas.append(
                            {
                                x: row[x],
                                y: row[y],
                                z: row[z],
                            }
                        )
                    print(pizzas)

            except FileNotFoundError:
                sys.exit("File does not exist")
            else:
                print(tabulate(pizzas, headers="keys", tablefmt="grid"))

        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
