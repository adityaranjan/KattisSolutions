#Kornislav
IntegerList = list(map(int, input().split(" ")))
IntegerList.sort()
Area = min([IntegerList[0], IntegerList[1]]) * min(IntegerList[2], IntegerList[3])
print(str(Area))