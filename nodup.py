#No Duplicates
Sentence = list(input().split(" "))
RepeatCheck = 0
for i in range(len(Sentence)):
    if Sentence[i] in Sentence:
        RepeatCheck += Sentence.count(Sentence[i])
if RepeatCheck > len(Sentence):
    print("no")
else:
    print("yes")