#answer to "Python > Basic Data Types > List Comprehensions"
#language: Python3

x = int(input().strip())
y = int(input().strip())
z = int(input().strip())
n = int(input().strip())

list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(list1)
