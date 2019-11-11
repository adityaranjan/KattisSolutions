#Cryptographer's Conundrum
Word = list(input())
DaysCount = 0
for i in range(int(len(Word) / 3)):
    if str(Word[3*i]).lower() != "p":
        DaysCount += 1
    if str(Word[(3*i) + 1]).lower() != "e":
        DaysCount += 1
    if str(Word[(3*i) + 2]).lower() != "r":
        DaysCount += 1
print(DaysCount)