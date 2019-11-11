#Cokolada
import math
List = []
BreaksNeeded = 0
SampleSquares = int(input())
result = False
i = 0
SquaresBuy = 0
while result == False:
    if (math.log(SampleSquares + i, 2)).is_integer():
        result = True
        SquaresBuy = SampleSquares + i
    i += 1
j = 0
RESULT = False
PiecesNeeded = 0
while RESULT == False:
    if (math.log(SampleSquares - j, 2)).is_integer() and ((SampleSquares) % (SampleSquares - j)) == 0:
        RESULT = True
        PiecesNeeded = SampleSquares - j
    j += 1
calc = int(SquaresBuy/PiecesNeeded)
BreaksNeeded = int(math.log(calc, 2))
print(str(SquaresBuy) + " " + str(BreaksNeeded))