class Underscore:
    def map(self, iterable, callback):
        aList = []
        for i in range(len(iterable)):
            aList.append(callback(iterable[i]))
        return(aList)

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if (callback(iterable[i])):
                return iterable[i]

    def filter(self, iterable, callback):
        aList = []
        for i in range(len(iterable)):
            if(callback(iterable[i])):
                aList.append(iterable[i])
        return aList

    def reject(self, iterable, callback):
        aList = []
        for i in range(len(iterable)):
            if(not callback(iterable[i])):
                aList.append(iterable[i])
        return aList


_ = Underscore()  # yes we are setting our instance to a variable that is an underscorecopy

# should return [2,4,6]
print(f"map returns: {_.map([1, 2, 3], lambda x: x*2)}")

# should return the first value that is greater than 4
print(f"find returns: {_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)}")

# should return [2,4,6]
print(f"filter returns:{_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)}")

# should return [1,3,5]
print(f"reject returns: {(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))}")
