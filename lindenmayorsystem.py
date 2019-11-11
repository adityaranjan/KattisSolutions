#Linden Mayor System
NumLines, NumIterations = map(int, input().split(" "))
LetterList = []
ReplaceList = []
for i in range(NumLines):
    Letter, Replace = input().split(" -> ")
    LetterList.append(Letter)
    ReplaceList.append(Replace)
Sequence = list(input())
for j in range(NumIterations):
    k = 0
    for k in range(len(Sequence)):
        a = 0
        for a in range(len(LetterList)):
            if Sequence[k] == LetterList[a]:
                Sequence[k] = ReplaceList[a]
                break
    #Joining elements of different sizes and then breaking it into a list of one letter per element
    Sequence = list(''.join(Sequence))
print(''.join(Sequence))