a = 50

while a > 0:
    print(f"Amount Due: {a}")
    b = int(input("Insert Coin: "))
    if b == 10 or b == 25 or b == 5:
        a -= b

print(f"Change Owed: {abs(a)}")
