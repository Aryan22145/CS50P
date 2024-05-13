def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# meal
def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)


# percent
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    p = p / 100
    return p


main()
