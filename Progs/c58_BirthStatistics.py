xs = []
ys = []

name = "Jose"
gender = "M"
state = "CA"

with open("../data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        line_split = line.strip().split(",")
        if line_split[1] == name and line_split[3] == gender and line_split[4] == state:
            xs.append(int(line_split[2]))
            ys.append(int(line_split[5]))
print(xs)
print(ys)

# You Better Watch the Video cuz I don't have that file here I can't run the code
#But I understood it.