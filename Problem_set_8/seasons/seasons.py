from datetime import date
import sys
import inflect


class Minutes:
    def __init__(self, d1, dtoday):
        self.d1 = d1
        self.dtoday = dtoday
        self.tdelta = self.delta(dtoday, d1)
        self.conv_words = self.convert(self.tdelta)

    def __str__(self):
        return f"{self.conv_words} minutes"

    # get birthday (d1) and today's date (dtoday)
    @classmethod
    def get(cls):
        try:
            d1y, d1m, d1d = input("Date of Birth: ").split('-')
            d1 = date(int(d1y), int(d1m), int(d1d))
        except ValueError:
            sys.exit("Invalid date")
        else:
            if len(d1y) != 4:
                sys.exit("Invalid date")
        dtoday = date.today()
        return cls(d1, dtoday)

    # get delta in minutes
    def delta(self, dtoday, d1):
        tdelta = (date.__sub__(dtoday, d1)).days*24*60
        return tdelta

    # convert num to words
    def convert(self, tdelta):
        conv_words = (inflect.engine().number_to_words(tdelta)).capitalize().replace(" and", "")
        return conv_words

def main():
    minutes = Minutes.get()
    print(minutes)


if __name__ == "__main__":
    main()
