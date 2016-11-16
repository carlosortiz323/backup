#answer to "Python > Strings > String Validators"
#language: Python3

s = input().strip()

flagList = {"isalnumFlag": False,"isalphaFlag": False,"isdigitFlag": False,"islowerFlag": False,"isupperFlag": False}
flagListKey = ['isalnumFlag','isalphaFlag','isdigitFlag','islowerFlag','isupperFlag']

def StringValTool(myString):
    for x in range(len(myString)):
        myChar = myString[x]
        if myChar.isalnum():
            flagList["isalnumFlag"] = True
        if myChar.isalpha():
            flagList["isalphaFlag"] = True
        if myChar.isdigit():
            flagList["isdigitFlag"] = True
        if myChar.islower():
            flagList["islowerFlag"] = True
        if myChar.isupper():
            flagList["isupperFlag"] = True


    for y in range(len(flagListKey)):
        print(flagList[flagListKey[y]])

StringValTool(s)
