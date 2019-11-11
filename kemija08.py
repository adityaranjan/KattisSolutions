#Kemija
VowelList = ["a", "e", "i", "o", "u"]
SimpleWordsList = []
WordsList = list(input().split(" "))
for i in range(len(WordsList)):
    LetterList = list(WordsList[i])
    SimpleWord = ""
    j = 0
    while j < len(LetterList):
        if LetterList[j] in VowelList:
            SimpleWord += LetterList[j]
            j += 3
        else:
            SimpleWord += LetterList[j]
            j += 1
    SimpleWordsList.append(SimpleWord)
print(str(' '.join(SimpleWordsList)))