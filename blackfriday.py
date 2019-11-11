#Black Friday
GroupSize = int(input())
OutcomeList = list(map(int, input().split(" ")))
UniqueList = []
for i in range(GroupSize):
    if OutcomeList.count(OutcomeList[i]) == 1:
        UniqueList.append(OutcomeList[i])
if len(UniqueList) == 0:
    print("none")
else:
    print(OutcomeList.index(max(UniqueList)) + 1)