import random


def main():
    level = get_level()
    a = []
    b = []
    for _ in range(10):
        a.append(generate_integer(level))
        b.append(generate_integer(level))
    score = 0
    for _ in range(10):
        count = 3
        while count > 0:
            try:
                ans = int(input(f"{a[_]} + {b[_]} = "))
            except ValueError:
                count -= 1
                print("EEE")
                continue
            if ans != a[_] + b[_]:
                print("EEE")
                count -= 1
            else:
                score += 1
                break

            if count == 0:
                print(f"{a[_]} + {b[_]} = ", a[_] + b[_])

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    return x


if __name__ == "__main__":
    main()
