#cont to c26ifelse

currency = "€"#(Alt + 0128)

if currency == "$":#(Shift + 4)
    print("US Dollar")
else:
    if currency == "¥":#(Alt + 0165)
        print("Japanese Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "฿":
                print("Thai Bhat")
#Cant find rupee symbol
#or with elif
#easier to understand
if currency == "$":#(Shift + 4)
    print("US Dollar")
elif currency == "¥":#(Alt + 0165)
    print("Japanese Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Bhat")
print()

age = 10
if age >5:
    print("age>5")
elif age>8:
    print("age>8")
elif age>10:
    print("age>10")
else:
    print("Idiot, This wont print")


