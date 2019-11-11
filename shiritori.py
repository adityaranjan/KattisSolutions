#Shiritori
NumWords = int(input())
Count = 0
WordList = {}
LastLetter = ""
for i in range(NumWords):
    word = input()
    if i % 2 == 0:
        Player = 1
    else:
        Player = 2
    if i != 0:
        if word[:1] != LastLetter or word in WordList.keys():
            Count += 1
            print("Player " + str(Player) + " lost")
            break
    LastLetter = word[-1:]
    WordList[word] = ""
if Count == 0:
    print("Fair Game")