#How Many Digits?
import sys
import math
for line in sys.stdin:
    Number = int(line)
    if Number == 0 or Number == 1:
        print("1")
    else:
        print(math.floor((math.log10(Number * 2 * math.pi) * 0.5) + ((math.log10(Number) - math.log10(math.e)) * Number) + 1))