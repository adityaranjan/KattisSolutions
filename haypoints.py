#Hay Points
HayMoneyDictionary = {}
NumWords, NumJobDescriptions = map(int, input().split(" "))
for i in range(NumWords):
    HayWord, WordMoney = input().split(" ")
    HayMoneyDictionary[HayWord] = int(WordMoney)
for j in range(NumJobDescriptions):
    a = 0
    Salary = 0
    while True:
        Line = input()
        if Line != ".":
            TempList = list(Line.split(" "))
            for a in range(len(TempList)):
                Word = TempList[a]
                if Word in HayMoneyDictionary.keys():
                    Salary += HayMoneyDictionary[Word]
        elif Line == ".":
            print(Salary)
            break