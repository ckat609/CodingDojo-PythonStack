def reverseList(aList):
    length = len(aList)
    for i in range(length):
        aList[i], aList[length-i-1] = aList[length-i-1], aList[i]
        if(i == int(length/2)):
            break
    # print(length)
        # length -= 1
    return aList


print(reverseList([1, 3, 5, 7, 11, 13, 17]))


def isPalindrome(aString):
    for i in range(len(aString)):
        if(aString[i] != aString[len(aString) - i - 1]):
            return False
    return True


print(isPalindrome("otto"))


def assertEqual(coins):
    if(isinstance(coins, float)):
        coins *= 100
    change = []
    change.append(int(coins/25))
    change.append(int((coins - change[0]*25)/10))
    change.append(int((coins - (change[0]*25) - (change[1]*10))/5))
    change.append((coins - (change[0]*25) - (change[1]*10) - (change[2]*5)))

    return change


print(assertEqual(87))


def factorial(num):
    if(num > 1):
        num *= factorial(num-1)
    return num


print(factorial(5))


def fib(num1, num2, steps):
    if(num1 == 0):
        num1 = 1

    # num1 = num2
    if(steps > 0):
        num1 = num2
        num2 = num1 + fib(num1, num2, steps-1)
        print(num2)
    return num2


print(fib(0, 1, 10))
