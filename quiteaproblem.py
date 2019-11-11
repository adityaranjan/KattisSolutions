#Quite A Problem
import sys
for line in sys.stdin:
    ProblemCheck = 0
    ProblemWord = ""
    Line = list(line)
    for i in range(len(Line) - 6):
        ProblemWord = str(Line[i]) + str(Line[i+1]) + str(Line[i+2]) + str(Line[i+3]) + str(Line[i+4]) + str(Line[i+5]) + str(Line[i+6])
        if ProblemWord.lower() == "problem":
            ProblemCheck += 1
    if ProblemCheck > 0:
        print("yes")
    else:
        print("no")