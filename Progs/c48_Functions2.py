def multi_print(name,count):
    for i in range(0,count):#or range(1,count+1):
        print(name)

multi_print("Hansika",6)
print()
def another_function():
    multi_print("Hello",3)
    multi_print("World",3)

another_function()
print()

def maximum(a,b):
    if a < b:
        return b
    else:
        return a
result = maximum(152,153)
print(result)