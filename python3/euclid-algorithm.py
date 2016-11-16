def euclidAlgorithm(num1,num2):
  while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
  return num1

print(euclidAlgorithm(12,36))
