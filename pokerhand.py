#Poker Hand
CardsHand = list(input())
Ranks = []
UniqueList = []
CountList = []
for i in range(5):
    Ranks.append(CardsHand[i * 3])
    if Ranks[i] not in UniqueList:
        UniqueList.append(Ranks[i])
for k in range(len(UniqueList)):
    CountList.append(Ranks.count(UniqueList[k]))
print(max(CountList))