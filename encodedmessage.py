#Encoded Message
NumTestCases = int(input())
for i in range(NumTestCases):
    EncodedWord = list(input())
    j = 0
    NewWord = ""
    for j in range(int(len(EncodedWord) ** 0.5)):
        k = int((len(EncodedWord) ** 0.5) - (j + 1))
        a = 0
        for a in range(int(len(EncodedWord) ** 0.5)):
            NewWord += str(EncodedWord[int(k + ((a) * int(len(EncodedWord) ** 0.5)))])
    print(NewWord)