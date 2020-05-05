def biggieSize(aList):
    for i in range(len(aList)):
        if(aList[i] > 0):
            aList[i] = "big"
    return aList


print(f"#1: {biggieSize([-1, 3, 5, -5])}")


def countPositives(aList):
    sum = 0
    for i in range(len(aList)):
        if(aList[i] > 0):
            sum += 1
    aList[len(aList)-1] = sum
    return aList


print(f"#2: {countPositives([-1,1,1,1])}")
print(f"#2: {countPositives([1,6,-4,-2,-7,-2])}")


def sumTotal(aList):
    sum = 0
    for i in range(len(aList)):
        sum += aList[i]

    return sum


print(f"#3: {sumTotal([1,2,3,4])}")
print(f"#3: {sumTotal([6,3,-2])}")


def average(aList):
    sum = 0
    for i in range(len(aList)):
        sum += aList[i]

    return sum/len(aList)


print(f"#4: {average([1,2,3,4])}")


def length(aList):
    return len(aList)


print(f"#5: {length([37,2,1,-9])}")
print(f"#5: {length([])}")


def minimum(aList):
    if(len(aList) == 0):
        return False
    else:
        min = aList[0]
        for i in range(len(aList)-1):
            if(min > aList[i+1]):
                min = aList[i+1]
        return min


print(f"#6: {minimum([37,2,1,-9])}")
print(f"#6: {minimum([])}")


def maximum(aList):
    if(len(aList) == 0):
        return False
    else:
        max = aList[0]
        for i in range(len(aList)-1):
            if(max < aList[i+1]):
                max = aList[i+1]
        return max


print(f"#7: {maximum([37,2,1,-9])}")
print(f"#7: {maximum([])}")


def ultimateAnalysis(aList):
    min = aList[0]
    max = aList[0]
    sum = aList[0]

    for i in range(len(aList)-1):
        if(min > aList[i+1]):
            min = aList[i+1]
        if(max < aList[i+1]):
            max = aList[i+1]
        sum += aList[i+1]

    return {'sumTotal': sum, 'average': sum/len(aList), 'minimum': min, 'maximum': max, 'length': len(aList)}


print(f"#9: {ultimateAnalysis([37,2,1,-9])}")


def reverseList(aList):
    length = len(aList) - 1
    for i in range(length):
        aList[i], aList[length] = aList[length], aList[i]
        if(i >= length):
            break
        length -= 1
    return aList


print(f"#9: {reverseList([37,2,1,-9,4,2,7,4,6,8,4])}")
