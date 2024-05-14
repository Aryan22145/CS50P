def main():
    name = input("Input: ")
    a = shortern(name)
    print(a)


def shortern(name):
    a = name
    a = a.replace("a", "")
    a = a.replace("e", "")
    a = a.replace("i", "")
    a = a.replace("o", "")
    a = a.replace("u", "")
    a = a.replace("A", "")
    a = a.replace("E", "")
    a = a.replace("I", "")
    a = a.replace("O", "")
    a = a.replace("U", "")
    return a


if __name__ == "__main__":
    main()
