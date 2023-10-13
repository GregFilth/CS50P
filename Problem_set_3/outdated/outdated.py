month_list =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = query(month_list)
    print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")

def query(list):
    while True:
        birthday = input("Date: ").strip()
        try:
            month, day, year = birthday.split("/")
            if int(month)<13 and int(day)<32:
                return [month, day, year]
        except:
            try:
                month, day, year = birthday.split(" ")
                if day[-1] == ",":
                    day = day.replace(',', '')
                    if month in list:
                        month = list.index(month) + 1
                        if int(month)<13 and int(day)<32:
                            return [month, day, year]
            except:
                pass

main()