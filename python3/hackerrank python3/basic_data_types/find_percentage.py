#answer to "Python > Basic Data Types > Find the percentage"
#language: Python3

from decimal import Decimal

my_dict = {}
numStudents = int(input().strip())
studentName = 0
studentScores = []
buffer1 = []
averageNum = 0
pickStudent = 0


for x in range(numStudents):
    buffer1 = input().strip().split()

    my_dict[buffer1[0]] = [float(buffer1[1]),float(buffer1[2]),float(buffer1[3])]
    buffer1 = []

pickStudent = input().strip()

buffer1 = my_dict[pickStudent]

averageNum = float((buffer1[0]+buffer1[1]+buffer1[2])/3)


print(format(averageNum,'.2f'))
