import random
import sys


def main():
    user_level = query("Level: ")

    random_number = random_num(user_level)

    while True:
        user_guess = query("Guess: ")
        if user_guess <= user_level:
            if random_number > user_guess:
                print("Too small!")
            elif random_number < user_guess:
                print("Too large!")
            elif random_number == user_guess:
                print("Just right!")
                break


def query(x):
    while True:
        try:
            num = int(input(x).strip())
        except EOFError:
            sys.exit
        except:
            pass
        else:
            if num > 0:
                break
    return num


def random_num(num):
    return random.randint(1, num)


if __name__ == "__main__":
    main()
