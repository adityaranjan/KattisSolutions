#Tri
Num1, Num2, Num3, = map(int, input().split(" "))
SolutionCount = 0
if Num1 + Num2 == Num3 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "+" + str(Num2) + "=" +str(Num3))
if Num1 - Num2 == Num3 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "-" + str(Num2) + "=" +str(Num3))
if Num1 * Num2 == Num3 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "*" + str(Num2) + "=" +str(Num3))
if Num1 / Num2 == Num3 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "/" + str(Num2) + "=" +str(Num3))
if Num2 + Num3 == Num1 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "=" + str(Num2) + "+" +str(Num3))
if Num2 - Num3 == Num1 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "=" + str(Num2) + "-" +str(Num3))
if Num2 * Num3 == Num1 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "=" + str(Num2) + "*" +str(Num3))
if Num2 / Num3 == Num1 and SolutionCount == 0:
    SolutionCount += 1
    print(str(Num1) + "=" + str(Num2) + "/" +str(Num3))