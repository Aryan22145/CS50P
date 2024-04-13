items = {}

while True:
    try:
        item = input().upper().strip()
        if item not in items.keys():
            items[item] = 1
        else:
            items[item] += 1
    except EOFError:
        for key, value in sorted(items.items()):
            print(value, key)
        print()
        break
    except KeyError:
        pass
