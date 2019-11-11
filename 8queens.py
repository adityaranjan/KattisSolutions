#Eight Queens
ChessBoard = {}
Xlist = []
Ylist = []
for i in range(8):
    TempList = list(input())
    j = 0
    for j in range(8):
        if TempList[j] == "*":
            Xlist.append(j)
            Ylist.append(i)
        ChessBoard[j, i] = TempList[j]
def CheckQueen(X, Y):
    CollisionCount = 0
    a = 1
    while True:
        if X + a > 7:
            break
        elif ChessBoard[X + a, Y] == "*":
            CollisionCount += 1
            break
        a += 1
    a = 1
    while True:
        if X - a < 0:
            break
        elif ChessBoard[X - a, Y] == "*":
            CollisionCount += 1
            break
        a += 1
    a = 1
    while True:
        if Y + a > 7:
            break
        elif ChessBoard[X, Y + a] == "*":
            CollisionCount += 1
            break
        a += 1
    a = 1
    while True:
        if Y - a < 0:
            break
        elif ChessBoard[X, Y - a] == "*":
            CollisionCount += 1
            break
        a += 1
    a = 1
    b = 1
    while True:
        if X + a > 7 or Y - b < 0:
            break
        elif ChessBoard[X + a, Y - b] == "*":
            CollisionCount += 1
            break
        a += 1
        b += 1
    a = 1
    b = 1
    while True:
        if X + a > 7 or Y + b > 7:
            break
        elif ChessBoard[X + a, Y + b] == "*":
            CollisionCount += 1
            break
        a += 1
        b += 1
    a = 1
    b = 1
    while True:
        if X - a < 0 or Y + b > 7:
            break
        elif ChessBoard[X - a, Y + b] == "*":
            CollisionCount += 1
            break
        a += 1
        b += 1
    a = 1
    b = 1
    while True:
        if X - a < 0 or Y - b < 0:
            break
        elif ChessBoard[X - a, Y - b] == "*":
            CollisionCount += 1
            break
        a += 1
        b += 1
    return CollisionCount
QueenCheck = 0
for k in range(len(Xlist)):
    if CheckQueen(Xlist[k], Ylist[k]) > 0:
        break
    else:
        QueenCheck += 1
if QueenCheck == 8:
    print("valid")
else:
    print("invalid")