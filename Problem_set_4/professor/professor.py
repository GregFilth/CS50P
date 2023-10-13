import sys
import random


def main():
    score = 0
    u_level = get_level()
    for j in range(10):
        x = generate_integer(u_level)
        y = generate_integer(u_level)

        for k in range(3):
            answer = int(input(f"{x} + {y} = ").strip())
            if answer == (x + y):
                score += 1
                break
            else:
                print("EEE")
                if k == 2:
                    print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            g_level = int(input("Level: ").strip())
        except EOFError:
            sys.exit
        except:
            pass
        else:
            if 0 < g_level < 4:
                break
    return g_level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(
            int("1" + "0" * (level - 1)), int("9" + "9" * (level - 1))
        )


if __name__ == "__main__":
    main()
