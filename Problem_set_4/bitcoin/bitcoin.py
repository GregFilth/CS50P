import requests
import json
import sys


def main():
    try:
        num_bc = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.RequestException:
            sys.exit("Wrong request URL")
        else:
            o = response.json()
            rate = o["bpi"]["USD"]["rate_float"]
            cost = str(round((rate * num_bc), 4))
            print("$" + cost[:-8] + "," + cost[-8:])


if __name__ == "__main__":
    main()
