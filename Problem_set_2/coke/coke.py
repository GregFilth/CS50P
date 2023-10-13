amount = 0
due = 50
while(amount<50):
    due = 50 - amount
    print(f"Amount Due: {due}")
    inserted = int(input("Insert Coin: "))
    if inserted == 25 or inserted == 10 or inserted == 5:
        amount = amount + inserted

if amount >= 50:
    change = amount - 50
    print(f"Change Owed: {change}")