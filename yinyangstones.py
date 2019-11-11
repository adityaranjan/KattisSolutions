#Yin and Yang Stones
StonesList = list(input())
WhiteCount = 0
BlackCount = 0
for i in range(len(StonesList)):
    if StonesList[i] == "W":
        WhiteCount += 1
    else:
        BlackCount += 1
if WhiteCount == BlackCount:
    print("1")
else:
    print("0")