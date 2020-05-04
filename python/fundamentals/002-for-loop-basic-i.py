def basic(dispNumber):
    for i in range(dispNumber+1):
        print(i)
    return dispNumber


basic(150)


def multiplesOfFive(dispNumberMin, dispNumberMax, multipleOf):
    for i in range(dispNumberMin, dispNumberMax+1):
        if(i % multipleOf == 0):
            print(f"{i} is a multiple of {multipleOf}")


multiplesOfFive(5, 1000, 5)


def countingDojoWay(dispNumberMin, dispNumberMax):
    for i in range(dispNumberMin, dispNumberMax+1):
        if(i % 10 == 0):
            print(f"{i} Dojo")
        elif (i % 5 == 0):
            print(f"{i} Coding")


countingDojoWay(1, 100)


def sucker(maxNumber):
    sum = 0
    for i in range(maxNumber+1):
        if(i % 2 != 0):
            sum += i
    return sum


print(sucker(500000))


def countdown(startNum, step):
    step *= -1
    for i in range(startNum, 0, step):
        print(i)


countdown(2018, 4)


def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if(i % mult == 0):
            print(i)


flexibleCounter(2, 9, 3)
