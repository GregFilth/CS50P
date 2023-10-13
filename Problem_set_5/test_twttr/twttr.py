vowels_list = ["A", "E", "O", "I", "U", "a", "e", "o", "i", "u"]


def main():
    user_text = input("Input: ").strip()
    print(f"Output: {shorten(user_text)}")


def shorten(word):
    new_text = ""
    for i in range(len(word)):
        charact = word[i]
        if charact not in vowels_list:
            new_text = new_text + charact
    return new_text


if __name__ == "__main__":
    main()
