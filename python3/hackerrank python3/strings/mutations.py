#answer to "Python > Strings > Mutations"
#language: Python3


input1 = input().strip()
l1 = list(input1)
input2 = input().strip().split()

l1[int(input2[0])] = input2[1]

input1 = ''.join(l1)

print(input1)
