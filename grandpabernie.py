tripsDict = {}
numTrips = int(input())

for i in range(numTrips):
    country, year = input().split(" ")
    if country not in tripsDict.keys():
        tripsDict[country] = [int(year)]
    else:
        tripsDict[country].append(int(year))


numQueries = int(input())
sortedSet = set()

for j in range(numQueries):
    country, index = input().split(" ")
    if country not in sortedSet:
        tripsDict[country].sort()
        sortedSet.add(country)
    print(tripsDict[country][int(index) - 1])