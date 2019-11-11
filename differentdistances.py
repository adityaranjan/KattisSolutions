import math
result = False
while result == False:
    line = input()
    if line != "0":
         x1, y1, x2, y2, p = map(float, line.split(" "))
         output = (((abs(x1-x2)**p) + abs(y1-y2)**p))**(1/p)
         print(format(output, '.9f'))
    else:
         result = True