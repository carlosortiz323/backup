#answer to "Python > Basic Data Types > Tuples"
#language: Python3

n1 = int(input().strip())
l1 = input().strip().split()
l2 = []

for x in range(0,n1):
    l2.append(int(l1[x]))

t2 = tuple(l2)
print(hash(t2))
