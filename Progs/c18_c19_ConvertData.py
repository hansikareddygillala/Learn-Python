#Int to String
#str() will convert integer to string
a = 5
b = 10
print(f"Integer {a+b}")
print(f"String {str(a) + str(b)}")
print()

#String to int
a = "3"
b = "6"
print(f"String {a+b}")
print(f"Integer {int(a) + int(b)}")
print()

#Int to float
a = 8
print("Float",float(a))
b= 3.9
print(int(b))#prints only integer part
print()

#List to String
students = ["Apple","Mango","Banana","Orange"]
Students_as_string = " < ".join(students)
print(Students_as_string)
Students_as_string = ", ".join(students)
print(Students_as_string)
print()

#String to List
i ="a, b, c, d"
print(i.split(", "))
b = "I am a sentence with many words ."
print(len(b))
print(b.split(" "))
print(Students_as_string.split(", "))
print(len(Students_as_string.split(", ")))