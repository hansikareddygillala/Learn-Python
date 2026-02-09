#Continue will stop the loop there midway and iterate the next loop
for i in range(0,10):
    if i == 3:
        print("I skipped on 3")
        continue
    print(i)#3 does not print cuz continue
print()

#Break will stop the loop and will not iterate the next values it stops there
for i in range(0,10):
    if i == 3:
        print("I break on 3")
        break
    print(i)#3 does not print cuz break
print()
#Break Example
lww = [55,36,59,129,59]#list with weight
tw = 0#total weight
for e in lww:#element
    tw += e
    print(tw)
    if tw >200:#if max wt is 200 you can exit ryt
        print("Elevator Overload. Above 200kg")
        print("Last person who enetered should get out!")
        break

