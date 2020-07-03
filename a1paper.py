#A1 Paper
numPapers = int(input())
papersList = list(map(int, input().split(" ")))
tape, numNeed = 0, 2
possible = False

for i in range(numPapers - 1):
    tape += ((2 ** -0.75) / (2 ** (0.5 * i))) * (numNeed / 2)
    numNeed = (numNeed - papersList[i]) * 2
    if numNeed < 1:
        possible = True
        print(tape)
        break
    
if possible == False:
    print("impossible")
    
#SOLVED