#Birds on a Wire
l, d, n = map(int, input().split(" "))
PositionList = [6, l - 6]
BirdCount = 2
for i in range(n):
    PositionList.append(int(input()))
PositionList.sort()
for j in range(len(PositionList) - 1):
        BirdCount += ((PositionList[j + 1] - PositionList[j]) // d) - 1
print(BirdCount)