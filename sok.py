#Sok
AmountList = list(map(int, input().split(" ")))
RatioList = list(map(int, input().split(" ")))
QuotientList = []
LeftOverList = []
for i in range(3):
    QuotientList.append(float(AmountList[i]/RatioList[i]))
Factor = min(QuotientList)
for j in range(3):
    LeftOverList.append(str(float(AmountList[j] - (Factor * RatioList[j]))))
print(' '.join(LeftOverList))