#Greedily Increasing Subsequence
N = int(input())
NumList = list(map(int, input().split(" ")))
GIS = []
Max = NumList[0]
GIS.append(Max)
for i in range(N - 1):
    if NumList[i + 1] > Max:
        Max = NumList[i + 1]
        GIS.append(Max)
print(len(GIS))
print(' '.join(str(a) for a in GIS))