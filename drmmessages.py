#DRM Messages
import string
AlphabetList = list(string.ascii_uppercase)
InputList = list(input())
FirstString = list(InputList[:(int(len(InputList) / 2))])
SecondString = list(InputList[(int(len(InputList) / 2)):])
SumOne = 0
SumTwo = 0
for a in range(len(FirstString)):
    SumOne += AlphabetList.index(FirstString[a])
for b in range(len(SecondString)):
    SumTwo += AlphabetList.index(SecondString[b])
for x in range(len(FirstString)):
    if AlphabetList.index(FirstString[x]) + SumOne > 25:
        FirstString[x] = AlphabetList[(AlphabetList.index(FirstString[x]) + SumOne) % 26]
    else:
        FirstString[x] = AlphabetList[AlphabetList.index(FirstString[x]) + SumOne]
for y in range(len(SecondString)):
    if AlphabetList.index(SecondString[y]) + SumTwo > 25:
        SecondString[y] = AlphabetList[(AlphabetList.index(SecondString[y]) + SumTwo) % 26]
    else:
        SecondString[y] = AlphabetList[AlphabetList.index(SecondString[y]) + SumTwo]
for z in range(len(FirstString)):
    if AlphabetList.index(FirstString[z]) + AlphabetList.index(SecondString[z]) > 25:
        FirstString[z] = AlphabetList[(AlphabetList.index(FirstString[z]) + AlphabetList.index(SecondString[z])) % 26]
    else:
        FirstString[z] = AlphabetList[AlphabetList.index(FirstString[z]) + AlphabetList.index(SecondString[z])]
print(''.join(FirstString))