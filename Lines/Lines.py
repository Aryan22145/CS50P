import sys

if len(sys.argv) == 2:
    name = sys.argv[1]
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")


if not name.endswith(".py"):
    sys.exit("Not a python file")


try:
    file = open(name)
    lines = file.readlines()
    count = 0
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        elif line.isspace():
            continue
        else:
            count += 1
    file.close()
    print(count)
except FileNotFoundError:
    sys.exit("File doest not exist")
