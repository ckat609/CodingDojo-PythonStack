def selSort(aList):
    for i in range(len(aList)-1):
        for j in range(i+1, len(aList)):
            if(aList[i] > aList[j]):
                aList[i], aList[j] = aList[j], aList[i]
            print(aList)


selSort([36, 75, 82, 5, 17, 42, 81, 44, 93, 5, 43, 12, 64, 89, 34, 23, 63, 18, 94, 14, 25, 37])
