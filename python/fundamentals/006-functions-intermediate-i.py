import random
import math


def randInt(min=0, max=100):
    if(min > max or max < 0):
        return("Invalid min and max values")
    else:
        return (int(random.random() * (max-min+1)) + int(min))


print(randInt(50, 25))
print(randInt(50, -1))
print(randInt())
print(randInt(50))
print(randInt(min=25))
print(randInt(max=10))
# print(randInt(min=95))
