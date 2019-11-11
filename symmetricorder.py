#Symmetric Order
Result = False
SetNumber = 1
while Result == False:
    Line = int(input())
    if Line == 0:
        Result = True
    else:
        Store = [None] * Line
        OddNumberCounter = Line - 1
        i = 0
        for i in range(Line):
            Word = input()
            if i % 2 == 0:
                Store[int(i / 2)] = Word
            else:
                Store[OddNumberCounter] = Word
                OddNumberCounter -= 1
        print("SET " + str(SetNumber))
        j = 0
        for j in range(Line):
            print(Store[j])
    SetNumber += 1