#Relocation
N, Q = map(int, input().split(" "))
LocationList = list(map(int, input().split(" ")))
for i in range(Q):
    QueryType, A, B = map(int, input().split(" "))
    if QueryType == 1:
        LocationList[A - 1] = B
    elif QueryType == 2:
        print(abs(LocationList[A - 1] - LocationList[B - 1]))