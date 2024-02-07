def convert(a):
    b = a.replace(":)", "🙂")
    b = b.replace(":(", "🙁")
    return b


c = input("")
print(convert(c))
