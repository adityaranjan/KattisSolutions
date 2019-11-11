#The Amazing Human Cannonball
import math
NumTestCases = int(input())
for i in range(NumTestCases):
    V0, Angle, X1, H1, H2 = map(float, input().split(" "))
    T = X1 / (math.cos(math.radians(Angle)) * V0)
    Y = (V0 * T * math.sin(math.radians(Angle))) - (0.5 * 9.81 * (T ** 2))
    if Y >= H1 + 1 and Y <= H2 - 1:
        print("Safe")
    else:
        print("Not Safe")