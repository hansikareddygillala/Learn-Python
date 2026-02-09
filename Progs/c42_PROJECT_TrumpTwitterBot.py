'''
import --> used to import some module from your pc or it can be builtin module like numpy, random, etc
random --> It is a module to generate random numbers
randint --> Used to generate random integer in between two given numbers inclusively
len() --> Function that shows length or how many are there in it
import random
print(random.randint(0,4)) --> prints random integer between 0 and 4

'''
#------------TRUMP TWITTER BOT------------
import random
#Creating lists of terms for our tweets
part1 = ["Putin ", "Hilary ", "Obama ", "Fake News ", "Mexico ", "Arnold Schwarzenegger ", "The Democrats "]#7
part2 = ["no talent, ", "on the way down, ", "really poor numbers, ", "nasty tone, ", "looking like a fool, ","bad hombre, "]#6
part3 = ["got destroyed by my ratings. ", "rigged the election. ", "had a much smaller crowd. ","will pay for the wall. "]#4
part4 = ["So sad", "Apologize","So true","Media won't report","Big trouble", "Fantastic job", "Stay tuned"]#7

best_words = [part1,part2,part3,part4]#Nested List
#print(best_words)

for part in best_words:
    #print(len(part))#length of the part that in o/p shows 7647
    r = random.randint(0,len(part)-1)
    #print(part)#prints part1 part2 etc
    #print(r)#prints generated random integer
    print(part[r],end="")#prints the element in the index pos chosen by random i.e, in r
print()
'''
#OR printing snetence other method withour end
sentence = []
for part in best_words:
    r = random.randint(0,len(part)-1)
    sentence.append(part[r])
print(sentence)
print(" ".join(sentence))
'''