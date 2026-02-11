"""
csv --> comma separated value
"""
with open("file.csv") as file:
    for line in file:
        data = line.strip().split(",")
        #print(data)
        print(data[0] + " has " + data[1] + " rupees. \nName Shortcut " + data[2] + "\n")

