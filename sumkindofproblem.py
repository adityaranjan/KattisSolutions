#Sum Kind of Problem
NumDataSets = int(input())
for i in range(NumDataSets):
    DataSetNumber, NumIntegers = map(int, input().split(" "))
    OddSum = NumIntegers ** 2
    EvenSum = OddSum + NumIntegers
    PositiveSum = int(EvenSum / 2)
    print(str(DataSetNumber) + " " + str(PositiveSum) + " " + str(OddSum) + " " + str(EvenSum))