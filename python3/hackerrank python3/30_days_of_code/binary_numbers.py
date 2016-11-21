#answer to "Tutorials > 30 Days of Code > Day 10:Binary Numbers"
#language: Python3

import sys

n = int(input().strip())
wasOne = False
tempOccur = 0
numOccur = 0


binaryString = "{0:#b}".format(n)
#print(binaryString)

for i in range(2,len(binaryString),1):
    if binaryString[i] == "1" and wasOne == True:
        tempOccur += 1
        wasOne = True
    elif binaryString[i] == "1" and wasOne == False:
        tempOccur = 1
        wasOne = True
    elif binaryString[i] == "0":
        tempOccur = 0
        wasOne = False
    if tempOccur > numOccur:
        numOccur = tempOccur
print(numOccur)
