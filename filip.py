#Filip
NumOne, NumTwo = input().split(" ")
NumberOne = int(str(NumOne)[::-1])
NumberTwo = int(str(NumTwo)[::-1])
if NumberOne > NumberTwo:
    print(str(NumberOne))
else:
    print(str(NumberTwo))