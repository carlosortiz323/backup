#answer to "Tutorials > 30 Days of Code > Day 8:Dictionaries and Maps"
#language: Python3

numEntries = int(input().strip())
phoneBook = {}

for i in range(numEntries):
    entry = input().strip().split()
    phoneBook[entry[0]] = entry[1]

for i in range(numEntries):
    lookup = input().strip()
    if lookup in phoneBook:
        print(lookup + "=" + phoneBook[lookup])
    else:
        print("Not found")
