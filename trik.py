#Trik
Moves = list(input())
CupPosition = 1
for i in range(len(Moves)):
    if CupPosition == 1 and Moves[i] == "A":
        CupPosition += 1
    elif CupPosition == 2 and Moves[i] == "A":
        CupPosition -= 1
    if CupPosition == 2 and Moves[i] == "B":
        CupPosition += 1
    elif CupPosition == 3 and Moves[i] == "B":
        CupPosition -= 1
    if CupPosition == 1 and Moves[i] == "C":
        CupPosition += 2
    elif CupPosition == 3 and Moves[i] == "C":
        CupPosition -= 2
print(CupPosition)