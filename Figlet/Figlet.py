import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandom = False
else:
    sys.exit(1)

a = input("Input: ")

figlet.getFonts()
if not isRandom:
    try:
        figlet.setFont(font = sys.argv[-1])
        print(figlet.renderText(a))
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    b = random.choice(figlet.getFonts())



print(f"Output: {figlet.renderText(a)}")



