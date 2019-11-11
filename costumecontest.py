#Costume Contest
N = int(input())
AllCostumeList = []
UniqueCostumeList = []
CountList = []
OutputList = []
for i in range(N):
    Costume = input()
    if Costume not in UniqueCostumeList:
        UniqueCostumeList.append(Costume)
    AllCostumeList.append(Costume)
for j in range(len(UniqueCostumeList)):
    CountList.append(AllCostumeList.count(UniqueCostumeList[j]))
for k in range(len(CountList)):
    if CountList[k] == min(CountList):
        OutputList.append(UniqueCostumeList[k])
OutputList.sort()
for a in range(len(OutputList)):
    print(OutputList[a])