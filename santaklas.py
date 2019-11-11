#Santa Klas
import math
height, degree = map(int, input().split(" "))
if degree >= 0 and degree <= 180:
    print("safe")
elif degree == 270:
    print(height)
elif degree > 180 and degree < 270:
    print(math.floor(height/(math.cos(math.radians(270 - degree)))))
elif degree > 270 and degree <= 359:
    print(math.floor(height/(math.cos(math.radians(degree - 270)))))