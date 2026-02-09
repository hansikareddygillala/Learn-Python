
#TASK 1
continents = ["Africa", "Antarctica", "Asia", "Australia and Oceania", "Europe", "North America", "South America"]
#a)
#continents.pop(1)
#for continent in continents:
#    print(continent)
#b)
stuff_inc = []
stuff = ["Asia", "Max", 101, "Monika", "China", "Simbabwe", "Antarctica"]
for i in stuff:
    for j in continents:
        if i==j:
            print(i)
            stuff_inc.append(i)
print(len(stuff_inc))

#TASK 2
while True:
    c = int(input("Enter item cost: "))#cost
    dp = 0#discounted price
    if 0<=c<=20:
        dp = c-c*20/100
    elif 20<c<=50:
        dp = c-c*40/100
    else:
        dp = c-c*60/100
    print(dp)
    continue