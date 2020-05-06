x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


def changeValInList(oldValue, newValue, listToModify):
    for i in range(len(listToModify)):
        for j in range(len(listToModify[i])):
            if(listToModify[i][j] == oldValue):
                listToModify[i][j] = newValue
    return listToModify


def renameStudent(fromName, toName, listToModify):
    for i in range(len(listToModify)):
        if(listToModify[i]['last_name'] == fromName):
            listToModify[i]['last_name'] = toName
    return (listToModify)


def renamePlayer(fromName, toName, listToModify):
    for sport in listToModify:
        for i in range(len(listToModify[sport])):
            if(listToModify[sport][i] == fromName):
                listToModify[sport][i] = toName
    return (listToModify)


def changeValue(oldValue, newValue, listToModify):
    for i in listToModify:
        for j in i:
            if(i[j] == oldValue):
                i[j] = newValue

    return listToModify


print(f"#1-1: Value was changed to: {changeValInList(10, 15, [[5, 2, 3], [10, 8, 9], [6, 7, 10], [1, 10, 9]])}")
# print(f"#1-2: Name was changed to: {renameStudent('Jordan', 'Bryant', students)}")
# print(f"#1-3: Name was changed to: {renamePlayer('Messi', 'Andres', sports_directory)}")
# print(f"#1-4: Value was changed to: {changeValue(20, 30, z)}")
print("-----------------------------------------")

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def iterateDictionary(listToModify):
    output = "\n"
    for student in listToModify:
        count = 1
        for key, value in student.items():
            output += f"{key} - {value}"
            output += "\n" if (count == len(student)) else ", "
            count += 1
    return output


def iterateDictionary2(key_name, some_list):
    output = ""
    for i in some_list:
        if (key_name in i):
            output += i[key_name] + "\n"
            # print(i[key_name])
    return output


def printInfo(some_list):
    content = "\n"
    for key, value in some_list.items():
        content += (f"{len(value)} {key}\n").upper()
        for item in value:
            content += item + "\n"
        content += "\n"
    return content


print(f"#2: {iterateDictionary(students)}")
print(f"#3: {iterateDictionary2('first_name', students)}")
print(f"#3: {iterateDictionary2('last_name', students)}")
print(f"#4: {printInfo(dojo)}")
