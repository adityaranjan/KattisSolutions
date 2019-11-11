NumCases = int(input())
for i in range(NumCases):
    DifferenceList = []
    Sequence = list(map(int, input().split(" ")))
    SequenceLength = Sequence[0]
    del Sequence[0]
    j = 0
    for j in range(SequenceLength - 1):
        DifferenceList.append(abs(Sequence[j + 1] - Sequence[j]))
    k = 0
    EqualCount = 0
    for k in range(SequenceLength - 2):
        if DifferenceList[k] == DifferenceList[k + 1]:
            EqualCount += 1
    DifferenceList.clear()
    Sequence.sort()
    SortEqualCount = 0
    a = 0
    if EqualCount != SequenceLength - 2:
        for a in range(SequenceLength - 1):
            DifferenceList.append(abs(Sequence[a + 1] - Sequence[a]))
        b = 0
        for b in range(SequenceLength - 2):
            if DifferenceList[b] == DifferenceList[b + 1]:
                SortEqualCount += 1
    if EqualCount == SequenceLength - 2:
        print("arithmetic")
    elif SortEqualCount == SequenceLength - 2:
        print("permuted arithmetic")
    else:
        print("non-arithmetic")