#Tai's Formula
NumInputs = int(input())
Xlist = []
Ylist = []
Area = 0
for i in range(NumInputs):
    X, Y = map(float, input().split(" "))
    Xlist.append(X)
    Ylist.append(Y)
for j in range(NumInputs - 1):
    Area += (Xlist[j + 1] - Xlist[j]) * ((Ylist[j] + Ylist[j + 1])/2)
print(Area/1000)