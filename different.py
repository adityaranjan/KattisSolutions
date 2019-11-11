#A Different Problem
import sys
for line in sys.stdin:
    NumOne, NumTwo = map(int, str(line).split(" "))
    print(str(abs(NumOne - NumTwo)))