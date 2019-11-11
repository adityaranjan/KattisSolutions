#Stacking Cups
NumCups = int(input())
Cups = {}
for i in range(NumCups):
    X, Y = input().split(" ")
    if X.isalpha():
        Cups[int(Y)] = X
    else:
        Cups[int(int(X) / 2)] = Y
RadiiList = list(Cups.keys())
RadiiList.sort()
for j in range(NumCups):
    print(Cups[RadiiList[j]])