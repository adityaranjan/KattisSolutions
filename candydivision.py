#CandyDivision
import math
FactorList = []
D = int(input())
i = 1
while i <= math.floor(D ** 0.5):
    if D % i == 0 and i != D / i:
        FactorList.append(i)
        FactorList.append(int(D / i))
    elif D % i == 0 and i == D / i:
        FactorList.append(i)
    i += 1
for j in range(len(FactorList)):
    FactorList[j] -= 1
FactorList.sort()
print(' '.join(list(map(str, FactorList))))