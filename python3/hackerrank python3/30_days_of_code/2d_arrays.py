#answer to "Tutorials > 30 Days of Code > Day 11:2D Arrays"
#language: Python3

#!/bin/python3

import sys


givenArr = []
vertIndex = 0
horIndex = 0
sumArr = []
tempVal = 0

for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   givenArr.append(arr_t)

def FindTheI():
    arrOfI = [givenArr[vertIndex][horIndex],givenArr[vertIndex][horIndex+1],givenArr[vertIndex][horIndex+2],givenArr[vertIndex+1][horIndex+1],givenArr[vertIndex+2][horIndex],givenArr[vertIndex+2][horIndex+1],givenArr[vertIndex+2][horIndex+2]]

    #print(arrOfI)
    tempVal = 0
    for i in range(7):
        tempVal += arrOfI[i]
    sumArr.append(tempVal)
    #print(sumArr)

while vertIndex < 4 :
    
    
    if horIndex == 4:
        vertIndex += 1
        horIndex = 0
    else:
        #print(horIndex)
        FindTheI()
        horIndex += 1
print(max(sumArr))
#print(horIndex)
#print(vertIndex)
