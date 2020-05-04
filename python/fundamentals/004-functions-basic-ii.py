# 1
def countdown(maxNum):
    listDisplay = []
    for i in range(maxNum, 0, -1):
        listDisplay.append(i)

    return listDisplay


print(f"#1: {countdown(5)}")

# 2


def printAndReturn(aList):
    print(aList[0])
    return(aList[1])


print(f"#2: {printAndReturn([1, 2])}")

# 3


def printPlusLength(aList):
    return (len(aList) + aList[0])


print(f"#3: {printPlusLength([1, 2, 3, 4, 5])}")


# 4
def firstGreaterThanSecond(aList):
    sumGreater = 0
    newList = []

    if(len(aList) < 2):
        return False
    else:
        for i in range(len(aList)):
            if(aList[i] > aList[1]):
                sumGreater += 1
                newList.append(aList[i])
        print(sumGreater)
        return(newList)


print(f"#4: {firstGreaterThanSecond([5, 2, 3, 2, 1, 4])}")
print(f"#4: {firstGreaterThanSecond([3])}")

# 5


def thisLengthThatValue(num1, num2):
    newList = []
    for i in range(0, num1):
        newList.append(num2)
    return(newList)


print(f"#5 {thisLengthThatValue(4,7)}")
print(f"#5 {thisLengthThatValue(6,2)}")

