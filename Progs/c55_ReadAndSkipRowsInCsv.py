with open("file.csv") as file:
    for line in file:
        data = line.strip().split(",")
        #print(data)
        
        """
        if data[2] == "ABI" or data[2] == "BNU":
            print(data)
            print(data[2])
        """

        if int(data[1]) < 90:
            continue
        print(data)
        #print(int(data[1]))