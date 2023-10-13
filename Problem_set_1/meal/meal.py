def main():
    user_time = input("What time is it? ")
    decimal_time = convert(user_time)
    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    x, y = time.split(":")
    timedec = int(x) + (int(y)/60)
    return timedec


if __name__ == "__main__":
    main()