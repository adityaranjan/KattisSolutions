#Happy Happy Prime Prime
import math

def isPrime(number):
    if number == 1:
        return False
    else:
        for j in range(2, math.floor(number ** 0.5) + 1):
            if number % j == 0:
                return False
    return True
    
def isHappy(number):
    if number == 1:
        return True
    else:
        numList = [number]
        while True:
            sumNum = 0
            strNum = str(numList[-1])
            for i in range(len(strNum)):
                sumNum += int(strNum[i]) ** 2
            numList.append(sumNum)
            if numList[-1] == 1:
                return True
            if numList.count(numList[-1]) > 1:
                return False

numTestCases = int(input())
for k in range(numTestCases):
    caseNum, number = map(int, input().split(" "))
    if isPrime(number) and isHappy(number):
        print(str(caseNum) + " " + str(number) + " YES")
    else:
        print(str(caseNum) + " " + str(number) + " NO")