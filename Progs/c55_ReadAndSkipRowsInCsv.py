with open("file.csv") as file:
    for line in file:
        data = line.strip().split(",")
        #print(data)
        
        """
        if data[2] == "ABI" or data[2] == "BNU":
            print(data)
            print(data[2])
        """
#Prints who have more than 90 rupees (it gives their whole data)
        if int(data[1]) < 90:
            continue
        print(data)
        #print(int(data[1]))