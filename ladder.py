import math
xone, xtwo = map(int, input().split(" "))
print(str(math.ceil(float((xone / float((math.sin(math.radians(xtwo)))))))))