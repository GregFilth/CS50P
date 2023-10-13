camel_name = input("camelCase: ").strip()
snake_case = "" + camel_name
for i in range(len(camel_name)):
    if camel_name[i].isupper():
        lower_replacement = "_" + camel_name[i].lower()
        snake_case = snake_case.replace(camel_name[i], lower_replacement)
print(f"snake_case: {snake_case}")