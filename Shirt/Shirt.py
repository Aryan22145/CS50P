import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    first = sys.argv[1].split(".")[1]
    second = sys.argv[2].split(".")[1]
    if first == second:
        if second in ["jpg", "jpeg", "png"]:
            try:
                picture = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exist")
            shirt = Image.open("shirt.png")
            size = shirt.size
            doll = ImageOps.fit(picture, size)
            doll.paste(shirt, shirt)
            doll.save(sys.argv[2])
        else:
            sys.exit("Invalid Output")
    else:
        sys.exit("Input and output have different extensions")
elif len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


