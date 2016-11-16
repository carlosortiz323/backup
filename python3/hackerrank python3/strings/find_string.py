#answer to "Python > Strings > Find a string"
#language: Python3

bufferStr = input().strip()
matchStr = input().strip()
numOccur = 0
indexHolder = 0



for x in range(len(bufferStr)):
    if bufferStr[indexHolder:indexHolder + len(matchStr)] == matchStr:
        numOccur += 1
    indexHolder += 1
print(numOccur)
