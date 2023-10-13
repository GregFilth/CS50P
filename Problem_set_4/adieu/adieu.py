import inflect
import sys

p = inflect.engine()

def main():
    name_list=[]
    while True:

        try:
            new_name = input("Name: ").strip()
        except EOFError:
            break
        else:
            name_list.append(new_name)
            joined_list = p.join(name_list)
    if joined_list != []:
        print(f"Adieu, adieu, to {joined_list}")


if __name__ == "__main__":
    main()