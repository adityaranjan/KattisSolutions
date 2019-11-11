#Stand on Zanzibar
NumTestCases = int(input())
for i in range(NumTestCases):
    PopList = list(map(int, input().split(" ")))
    del PopList[len(PopList) - 1]
    j = 0
    ImportCount = 0
    for j in range(len(PopList) - 1):
        if PopList[j + 1] > (PopList[j] * 2):
            ImportCount += (PopList[j + 1] - (PopList[j] * 2))
    print(str(ImportCount))