import csv, sys


def main():
    students = []
    newheader = ["first", "last", "house"]

    if len(sys.argv) == 3:
        if sys.argv[1].strip().endswith(".csv") and sys.argv[2].strip().endswith(
            ".csv"
        ):
            # read the file and re-sort the columns into "first_name", "last_name" and "house"
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        l_n, f_n = str(row["name"]).split(", ")
                        students.append([f_n, l_n, row["house"]])

            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")

            # write into a new file
            with open(sys.argv[2], "w") as file0:
                writer = csv.writer(file0)
                writer.writerow(newheader)
                writer.writerows(students)

        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
