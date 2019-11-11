import string
NumCases = int(input())
for i in range(NumCases):
    AlphabetList = list(string.ascii_lowercase)
    MissingWord = ""
    Sentence = list(input())
    for j in range(len(Sentence)):
        value = str(Sentence[j]).lower() in AlphabetList
        if value == True:
            AlphabetList.remove(str(Sentence[j]).lower())
    for l in range(len(AlphabetList)):
        MissingWord += str(AlphabetList[l])
    if len(AlphabetList) > 0:
        print("missing " + str(MissingWord))
    else:
        print("pangram")