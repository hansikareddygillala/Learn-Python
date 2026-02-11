'''
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


cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]


def list_sum(l):
    total_price = 0
    for price in l:
        total_price += price
    print(total_price)


list_sum(cart_prices)



def prices_list(name, price):
    l =[]
    for i in range(0,11):
        multiprice = price*i
        l.append(str(i) + " x " + name + ": " + str(multiprice))
    return l

print(prices_list("Cookie", 0.79))
'''

shelf = ["Magic Mirror", "empty", "Cookie", "Book with Magic Tricks", "empty"]

def add_shelf(article):
    # Here comes your code
    # You can access the variable "shelf" directly from within the function
    # This does not have to be passed as a parameter, because it exists
    # outside of the function already.
    print("Here's where your code goes")

add_shelf("Rubik's Cube")
print(shelf)















