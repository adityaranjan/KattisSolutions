wordslist = list(str(input().split("-")))
wordslength = len(wordslist)
store = []
for i in range(int(wordslength)):
    if wordslist[i].isupper():
        store.append(str(wordslist[i]))
print (''.join(store))