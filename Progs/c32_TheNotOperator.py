#Membership Operator
age = 25
if not age >+30:
    print("executed")

#or
#this is efficient

if age< 30:
    print("executed")
print()

names = ["Max" ,"Nadine"]
if "Moe" not in names:
    print("Moe is not in the list")
#or(^ is efficient and easy to read)
if not "Moe" in names:
    print("Moe is not in the list")

if "Moe" in names:
    print("Moe is there")
else:
    print("Moe is not there")
    