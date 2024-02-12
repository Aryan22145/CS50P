import random
while True:
    try:
        a = int(input("Level: "))
        if a > 0:
            break
    except:
        continue

x = random.randint(0, a)


while True:
    try:
        b = int(input("Guess: "))
        if b != 0:
            if b < x:
                print("Too small!")
            elif b > x:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass

