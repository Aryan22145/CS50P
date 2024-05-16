import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    w = re.search(r'<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)"', s, re.IGNORECASE)
    if w:
        s = 'https://youtu.be/'+ w.group(1)
        return s


if __name__ == "__main__":
    main()
