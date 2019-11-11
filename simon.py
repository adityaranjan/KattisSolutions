#Simon Says
cases = int(input())
for i in range(cases):
    WordList = list(input().split(" "))
    if len(WordList) >= 2:
        if WordList[0] == "simon" and WordList[1] == "says":
            del WordList[0]
            del WordList[0]
            j = 0
            stringPrint = ""
            for j in range(len(WordList)):
                if j != len(WordList) - 1 and len(WordList) >= 1:
                    stringPrint += str(WordList[j]) + " "
                else:
                    stringPrint += str(WordList[j])
            print(stringPrint)
        else:
            print("")
        WordList.clear()