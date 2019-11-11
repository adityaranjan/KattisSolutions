#Krizaljka
A, B = input().split(" ")
ListA = list(A)
ListB = list(B)
for i in range(len(ListA)):
    if ListA[i] in ListB:
        Bposition = i
        Aposition = ListB.index(ListA[i])
        break
for j in range(len(ListB)):
    k = 0
    PrintList = []
    if j == Aposition:
        for k in range(len(ListA)):
            PrintList.append(ListA[k])
    else:
        for k in range(len(ListA)):
            if k == Bposition:
                PrintList.append(ListB[j])
            else:
                PrintList.append(".")
    print(''.join(PrintList))