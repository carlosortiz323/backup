#answer to "Tutorials > 30 Days of Code > Day 9:Recursion"
#language: Python3

numInput = int(input().strip())

def Factorial(numInput):
    total = 1
    if numInput == 0 or numInput == 1:
        return 1
    else:
        for i in range(numInput,0,-1):
            total *= i
    return total

print(Factorial(numInput))
