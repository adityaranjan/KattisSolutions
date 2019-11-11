#BeaverGnaw
import math
EndCheck = False
while EndCheck == False:
    D, V = map(int, input().split(" "))
    if D == 0 and V == 0:
        EndCheck = True
    else:
        print(str((D ** 3 - ((6 * V) / math.pi)) ** (1/3)))