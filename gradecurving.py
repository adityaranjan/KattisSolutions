#Grade Curving
import math
x, ylow, yhigh = map(int, input().split(" "))
klow = -1
i = 0
if yhigh == 100:
    while True:
        if math.ceil(x) >= ylow and math.ceil(x) <= yhigh:
            print(str(i) + " inf")
            break
        x = 10 * (x ** 0.5)
        i += 1
else:
    while True:
        if math.ceil(x) >= ylow and math.ceil(x) <= yhigh and klow == -1:
            klow = i
        if math.ceil(x) > yhigh and klow != -1:
            print(str(klow) + " " + str(i - 1))
            break
        if math.ceil(x) > yhigh and klow == -1:
            print("impossible")
            break
        x = 10 * (x ** 0.5)
        i += 1