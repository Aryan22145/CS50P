months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break

        elif "," in date:
            date = date.replace(",", "")
            month, date, year = date.split(" ")
            if month in months and int(day) <= 31:
                month = months.index(month) + 1

    except:
        print()
        pass

print(f"{int(year)}-{int(month):02}-{int(day):02}")
