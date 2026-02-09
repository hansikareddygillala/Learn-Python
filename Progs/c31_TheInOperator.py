#Membership Operator

students = ["Max","Monika","Erik","Franziska"]

print("Monika" in students)
print("Hansika" in students)
print()

if "Monika" in students:
    print("Yes, Monika studies here")

if "Hansika" in students:
    print("Yes,Hansika studies here")
else:
    print("No, Hansika does not study here")
print()

#This also works for strings
sentence = "Yes, Monika studies here!"
if "!" in sentence:
    print("Yes")
else:
    print("No")