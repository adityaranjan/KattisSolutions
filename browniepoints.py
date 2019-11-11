#Brownie Points 1
while True:
    line = int(input())
    if line == 0:
        break
    else:
        NumBrowniePoints = line
        Xlist = []
        Ylist = []
        Stan = 0
        Ollie = 0
        i = 0
        for i in range(NumBrowniePoints):
            x, y = map(int, input().split(" "))
            if i == ((NumBrowniePoints - 1) / 2):
                CenterX = x
                CenterY = y
            else:
                Xlist.append(x)
                Ylist.append(y)
        j = 0
        for j in range(len(Xlist)):
            if (Xlist[j] > CenterX and Ylist[j] > CenterY) or ((Xlist[j] < CenterX and Ylist[j] < CenterY)):
                Stan += 1
            elif (Xlist[j] > CenterX and Ylist[j] < CenterY) or ((Xlist[j] < CenterX and Ylist[j] > CenterY)):
                Ollie += 1
        print(str(Stan) + " " + str(Ollie))