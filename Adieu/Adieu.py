import inflect
a = inflect.engine()
b = []


while True:
    try:
        c = input("Name: ")
        b.append(c)

    except EOFError:
        print()
        break

list1 = a.join((b))
print("Adieu, adieu, to " + list1)



