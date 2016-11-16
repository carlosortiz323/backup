#answer to "Python > Basic Data Types > Nested Lists"
#language: Python3

numStudents = int(input().strip())
studentList = []
tempList = []
setList = []
duplList = []
numList = []


for x in range(numStudents):
    tempList.append(input().strip())
    tempList.append(float(input().strip()))
    studentList.append((tempList))
    tempList = []

studentList.sort(key=lambda x: x[1])

for x in studentList:
    numList.append(x[1])


for x in studentList:
    if x[1] not in setList:
        setList.append(x[1])

if numList.count(setList[1]) >=2:
    for x in range(len(numList)):
        if setList[1] == numList[x]:
            duplList.append(studentList[x][0])

    duplList.sort()

    print(duplList[0])
    print(duplList[1])
else:
    print(studentList[numList.index(setList[1])][0])
