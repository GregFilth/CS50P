

def main():
        fract = input("Fraction: ").strip()
        percent = convert(fract)
        print(gauge(percent))


def convert(fraction):
    x, y = fraction.split("/")
    while True:
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise ValueError
        else:
            if x<=y:
                try:
                    return round((x/y)*100)
                except ZeroDivisionError:
                    raise ZeroDivisionError
            elif y == 0:
                raise ZeroDivisionError
            else: raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()