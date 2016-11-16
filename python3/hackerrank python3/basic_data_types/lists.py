#answer to "Python > Basic Data Types > Lists"
#language: Python3

list1 = []
numLines = int(input().strip())
buffer1 = []

for x in range(0,numLines):
    buffer1 = input().strip().split()

    if buffer1[0] == 'insert':
        list1.insert(int(buffer1[1]),int(buffer1[2]))
    elif buffer1[0] == 'print':
        print(list1)
    elif buffer1[0] == 'remove':
        list1.remove(int(buffer1[1]))
    elif buffer1[0] == 'append':
        list1.append(int(buffer1[1]))
    elif buffer1[0] == 'sort':
        list1.sort()
    elif buffer1[0] == 'pop':
        list1.pop()
    elif buffer1[0] == 'reverse':
        list1.reverse()
