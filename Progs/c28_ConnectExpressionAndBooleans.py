age = 35
if age>=30 and age<=39:
    print("This is person is int heir 30s")
print()

age = 45
if age < 30 or age >=40:
    print("This person is not in their 30s")
print(age<30)
print(age>=40)
print()

age = 25
above_30 = age>=30
print(above_30)
print()

age = 25
above_20 = age >=20
print(above_20)
if age>=20:
    print("If statement was executed")
if True:
    print("Hi there")
if False:
    print("This statement wont print")
print()

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

country = "US"
age = 20
if (country == "US" and age >=21) or (country != "US" and age>=18):
    print("This person may drink alcohol")
else:
    print("This person may not drink alcohol")
