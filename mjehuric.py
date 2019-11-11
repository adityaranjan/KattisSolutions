#Mjehuric
PiecesList = list(map(int, input().split(" ")))
found = False
while found == False:
    if PiecesList == [1, 2, 3, 4, 5]:
        found = True
    else:
        i = 0
        for i in range(4):
            if PiecesList[i] > PiecesList[i + 1]:
                Temporary = PiecesList[i]
                PiecesList[i] = PiecesList[i + 1]
                PiecesList[i + 1] = Temporary
                print(' '.join(list(map(str, PiecesList))))