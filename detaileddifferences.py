#Detailed Differences
NumTestCases = int(input())
for i in range(NumTestCases):
    ListOne = list(input())
    ListTwo = list(input())
    DifferenceList = []
    j = 0
    for j in range(len(ListOne)):
        if ListOne[j] == ListTwo[j]:
            DifferenceList.append(".")
        else:
            DifferenceList.append("*")
    print(''.join(ListOne))
    print(''.join(ListTwo))
    print(''.join(DifferenceList))
    print("")