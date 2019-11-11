#Flexible Spaces
W, P = map(int, input().split(" "))
PartitionsList = list(map(int, input().split(" ")))
PartitionsList.insert(0, 0)
PartitionsList.append(W)
UniqueList = []
for i in range(P + 1):
    UniqueList.append(PartitionsList[i + 1])
for j in range(P):
    for k in range(P - j):
        difference = PartitionsList[k + j + 2] - PartitionsList[j + 1]
        if difference not in UniqueList:
            UniqueList.append(difference)
UniqueList.sort()
print(' '.join(str(a) for a in UniqueList))