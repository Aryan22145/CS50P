def main():
    greet = input("Greeting: ")
    a = value(greet)
    print(f"${a}")


def value(greet):
    x = greet.strip().lower()
    if x[0:5] == "hello":
        y = 0
        return y
    elif x[0] == "h":
        y = 20
        return y
    else:
        x = 100
        return x


if __name__ == "__main__":
    main()
