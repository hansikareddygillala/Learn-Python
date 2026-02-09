file = open("read.txt","r")

for line in file:
    print(line.strip())

file.close()
#Or you can write

with open("read.tst","r") as file:
    for line in file:
        print(line.strip())

#with keyword automatically closes the file which can avoid errors
