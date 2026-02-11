file = open("read.txt","r")

for line in file:
    print(line.strip())

file.close()

print()
print()
print()
print()

#Or you can write

with open("read.txt","r") as file:
    for line in file:
        print(line.strip())

#with keyword automatically closes the file which can avoid errors
