"""
file --> Is an object
w -->deletes everything in the file which is there before and will create a new file
a --> keeps everything that is there before and continues to edit the file
Now, if you change the w from the creating a file line to a then everytime you run the text will print below than editing it"""
file = open("write.txt","w")#Created a file and it will appear in the library (in write.txt file)

file.write("Hi!!!\n")#content in file
file.write("How are you?")#content in file
file.write("\n---------------------------------------------------------------------------------------------------------------------------------\n\n")

students = ["Max", "Monika", "Erik", "Franziska"]

for student in students:
    file.write(student + "\n")

file.write("\n---------------------------------------------------------------------------------------------------------------------------------\n\n")




file.close()#closing the file
