def main():
        percent = fraction_to_percent()
        if percent <= 1:
            print("E")
        elif percent >=99:
            print("F")
        else:
            print(f"{percent}%")

def fraction_to_percent():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x, y = fraction.split("/")
            if int(x)<=int(y):
                return round(int(x)/int(y)*100)
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()