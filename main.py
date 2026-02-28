jshshir = input("Enter JSHSHIR (14 digits): ").strip()

if not jshshir.isdigit():
    print("JSHSHIR must contain only digits.")
elif len(jshshir) != 14:
    print("JSHSHIR must be exactly 14 digits.")
else:
    year = jshshir[0:2]
    month = jshshir[2:4]
    day = jshshir[4:6]

    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
        print("Valid JSHSHIR format.")
    else:
        print("Invalid date section in JSHSHIR.")
