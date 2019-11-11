#Östgötska
WordCheck = 0
WordList = list(map(str, input().split(" ")))
for i in range(len(WordList)):
    if "ae" in WordList[i]:
        WordCheck += 1
if WordCheck >= (0.4 * len(WordList)):
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")