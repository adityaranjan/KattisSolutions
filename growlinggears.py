#Growling Gears
NumCases = int(input())
for i in range(NumCases):
    MaxValList = []
    NumGears = int(input())
    for j in range(NumGears):
        a, b, c = map(int, input().split(" "))
        MaxValList.append((((b / (2 * a)) ** 2) * (a * -1)) + ((b ** 2) / (2 * a)) + c)
    print(MaxValList.index(max(MaxValList)) + 1)