def insSort(aList):
    for i in range(0, len(aList)-1):
        for j in range(i+1, 0, -1):
            if(aList[j] < aList[j-1]):
                aList[j], aList[j-1] = aList[j-1], aList[j]
            else:
                break
    # print(aList)
    return aList


print(f"{insSort([36, 75, 82, 52, 17, 42, 81, 44, 93, 5, 43, 12, 64, 89, 34, 23, 63, 18, 94, 14, 25, 37])}")
print(f"{insSort([5,4,3,2,1])}")


# agarro el valor
# lo comparo con el anterior
# si es menor, lo inserto
# si es mayor, paso al siguiente y regreso al paso 2
