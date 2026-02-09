
#Lists
print()
#Basic List
fam = ["Daddy","Mummy","Bro","Me"]
print(fam)

#finding length of the list
print("length of fam "+str(len(fam)))

#finding length of a specific index in the list
print("length of bro "+str(len(fam[2])))

#adding something(a unit/index) to fam(list)
fam.append("Stupid")
print("After append(adding Stupid)")
print(fam)
print("length of fam "+str(len(fam)))
print("Fam members:- ")
print(fam[0])
print(fam[1])
print(fam[2])
print(fam[3])
print(fam[4])
print(fam)

#removing something(a unit/index) from fam(list)
fam.pop()
print("After pop(stupid gone) because he is last")
print(fam)
print("Can also remove an item in the list by using indexing in pop function")

#Conveting list into a string
#join the items in the lists
fam_str = ", ".join(fam)
print(fam_str)

#Converting a list into string
#split the items in the string
print(fam_str.split(", "))

#In Operator
print("Me" in fam)
print("me" in fam)