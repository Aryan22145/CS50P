a = input("CamelCase: ").strip()

for c in a:
    if c.isupper():
        c = c.lower()
        print("_", sep="", end="")
    print(c, sep="", end="")
print()
