#answer to "Python > Basic Data Types > Find the Second Largest Number"
#language: Python3

totalNums = int(input().strip())

l1 = input().strip().split()

l2 = [int(x) for x in l1]

l3 = list(set(l2))

l3.sort()

print(l3[len(l3)-2])
