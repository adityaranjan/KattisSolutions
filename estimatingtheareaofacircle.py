#Estimating The Area Of A Circle
import math
result = True
while result == True:
    Input = input()
    if Input == "0 0 0":
        result = False
    else:
        Radius, TotalPoints, CirclePoints = map(float, Input.split(" "))
        TrueArea = float(math.pi * (Radius ** 2))
        EstimatedArea = float((CirclePoints/TotalPoints) * ((Radius * 2) ** 2))
        print(str(TrueArea) + " " + str(EstimatedArea))