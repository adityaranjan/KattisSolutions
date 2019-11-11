#Mirror Images
NumCases = int(input())
for i in range(NumCases):
    R, C = map(int, input().split(" "))
    ListOfRows = []
    print("Test " + str(i + 1))
    j = 0
    for j in range(R):
        ListOfRows.append(input())
    k = 0
    for k in range(R):
        temp = list(ListOfRows[len(ListOfRows) - k - 1])
        temp.reverse()
        print(''.join(temp))