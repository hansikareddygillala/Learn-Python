"""
S1 -> install matplotlib in Pycharm (I installed it on 12/26/2025 at around 10:30am).
S2 -> Import it to the program file.


"""

import matplotlib.pyplot as plt

x = [3,4,8] # x cordinates
y = [3,4,5] # y cordinates

plt.plot(x,y)

a = [2,0]
b = [6,0]
plt.plot(a,b)

#if it is a single point it wont show idk why
#Maybe because a point cont be known without thickness
plt.show()
