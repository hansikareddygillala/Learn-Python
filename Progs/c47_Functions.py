"""
FUNCTION
def -->defining something e.g. a function

-> Calling a function will execute the code inside the defined function block
-> name in second function is known

"""

print("Normal print statement")
print()

def multi_print():
    print("Inside function statement 1")
    print("Inside function statement 2")

multi_print()#calling the defines function
print()

def multi_print_2(name):
    print(name)
    print("My name is "+name)
multi_print_2("Hansika")
#multi_print("Hansika")#It will be an error because the parameters are not given
multi_print_2("Swapna")
