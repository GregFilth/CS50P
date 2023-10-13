import emoji

def main():
    text_with_emoticons = emoji.emojize(input("Input: "), language='alias')
    print(f"Output: {text_with_emoticons}")


if __name__ == "__main__":
    main()