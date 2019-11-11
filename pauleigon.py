#Paul Eigon
n, p, q = map(int, input().split(" "))
if ((p + q) // n) % 2 == 0:
    print("paul")
else:
    print("opponent")