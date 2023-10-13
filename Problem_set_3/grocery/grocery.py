def main():
    checklist = query()
    print()
    for key, value in checklist.items():
        print(value, key)


def query():
    groc_dict = {}
    while True:
        try:
            entry = (input().strip().upper())
        except EOFError:
            break
        if entry in groc_dict:
            groc_dict[entry] += 1
        else:
            groc_dict[entry] = 1
    groc_dict = dict(sorted(groc_dict.items()))
    return groc_dict

main()