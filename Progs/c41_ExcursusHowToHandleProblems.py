'''
print("Hello" + 13)
It will be error cuz int and str concatenation will not happen

ERROR SHOWN
    print("Hello" + 13)
          ~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str

Best Website to Rectify is "stackoverflow"

Debug:
cast it string by using str function
print("Hello" + str(13))
'''
print("Hello" + str(13))
