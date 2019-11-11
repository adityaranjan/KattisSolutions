import sys
for line in sys.stdin:
    NumList = list(str(line).split(" "))
    NewNumList = list(map(int, NumList))
    print(str(int(sum(NewNumList)/2)))