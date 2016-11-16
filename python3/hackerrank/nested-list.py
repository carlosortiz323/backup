numStudents = int(input().strip())
studentList = []
tempList = []
setList = []
duplList = []


for x in range(numStudents):
    tempList.append(input().strip())
    tempList.append(float(input().strip()))
    studentList.append((tempList))
    tempList = []

studentList.sort(key=lambda x: x[1])


#print(studentList)


for x in studentList:
    if x[1] not in setList:
        setList.append(x[1])


#print(type(setList[1]))
#print(type(setList[1]))


if studentList.count(setList[1]) >= 2:
    for x in studentList:
        if setList[1] == x:
            duplList.append(studentList[studentList.index(x)][0])

    duplList.sort()
    print(duplList[0])
    print(duplList[1])

else:
    print(studentList[studentList.index(setList[1])[0]])
