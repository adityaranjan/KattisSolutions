#Simon Says
cases = int(input())
for i in range(cases):
    WordList = list(input().split(" "))
    if WordList[0] == "Simon" and WordList[1] == "says" and len(WordList) > 2:
        del WordList[0]
        del WordList[0]
        j = 0
        stringPrint = ""
        for j in range(len(WordList)):
            if WordList[j] != WordList[len(WordList) - 1]:
                stringPrint += WordList[j] + " "
            else:
                stringPrint += WordList[j]
        print(stringPrint)