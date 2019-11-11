#Line Them Up
NumNames = int(input())
Count = 0
NameList = []
for i in range(NumNames):
    NameList.append(str(input()))
for j in range(NumNames - 1):
    if NameList[j] < NameList[j + 1]:
        Count += 1
    if NameList[j] > NameList[j + 1]:
        Count -= 1
if abs(Count) == NumNames - 1 and Count > 0:
    print("INCREASING")
elif abs(Count) == NumNames - 1 and Count < 0:
    print("DECREASING")
else:
    print("NEITHER")