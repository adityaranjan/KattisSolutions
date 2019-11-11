#Cetiri
NumberList = list(map(int, input().split()))
NumberList.sort()
DifferenceOne = NumberList[1] - NumberList[0]
DifferenceTwo = NumberList[2] - NumberList[1]
if DifferenceOne == DifferenceTwo * 2:
    print(str(NumberList[0] + DifferenceTwo))
elif DifferenceTwo == DifferenceOne * 2:
    print(str(NumberList[1] + DifferenceOne))
else:
    print(str(NumberList[2] + DifferenceOne))