"""
open --> it is a function that will open a file
r --> It allows us to read the file
"""

file = open("read.txt","r")#bought the file read.txt to this python program
'''
for line in file:#print the file
    print(line)
    print(len(line))


# if this block of code is executed a line break will be present for every
#To remove that we have to options
#1) write end=""
#   print(line,end="")
#2) write .strip()
#   print(line.strip())

for line in file:
    print(line,end="")
    print(len(line))
'''
for line in file:
    print(line.strip())
    print(len(line))
