#Free Food
NumEvents = int(input())
UnionSet = set()
for i in range(NumEvents):
    DayList = []
    DayOne, DayTwo = map(int, input().split(" "))
    while DayOne <= DayTwo:
        DayList.append(DayOne)
        DayOne += 1
        UnionSet = UnionSet.union(set(DayList))
print(len(UnionSet))