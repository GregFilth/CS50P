user_text = input("Input: ").strip()
new_text = ""
vowels_list = ["A", "E", "O", "I", "U", "a", "e", "o", "i", "u"]

for i in range(len(user_text)):
    charact = user_text[i]
    if charact not in vowels_list:
        new_text = new_text + charact
print(f"Output: {new_text}")