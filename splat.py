#Splat
import math
NumPaintings = int(input())
for i in range(NumPaintings):
    CenterX = []
    CenterY = []
    RadiusList = []
    ColorList = []
    NumDrops = int(input())
    j = 0
    for j in range(NumDrops):
        X, Y, V, Color = input().split(" ")
        CenterX.append(float(X))
        CenterY.append(float(Y))
        RadiusList.append(math.sqrt(float(V) / math.pi))
        ColorList.append(Color)
    NumQueries = int(input())
    k = 0
    for k in range(NumQueries):
        WhiteCheck = 0
        x, y = map(float, input().split(" "))
        OverlapColorList = []
        a = 0
        for a in range(NumDrops):
            if math.sqrt(((x - CenterX[a]) ** 2) + ((y - CenterY[a]) ** 2)) <= RadiusList[a]:
                OverlapColorList.append(ColorList[a])
            else:
                WhiteCheck += 1
        if WhiteCheck == NumDrops:
            print("white")
        else:
            print(OverlapColorList[len(OverlapColorList) - 1])