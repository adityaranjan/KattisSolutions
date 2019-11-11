#Hangman
word = list(input())
permutation = list(input())
i = 0
count = 0
hang = 0
while True:
    if permutation[i] in word:
        count += word.count(permutation[i])
    else:
        hang += 1
    if hang == 10:
        break
    if count == len(word):
        break
    i += 1
if count == len(word):
    print("WIN")
else:
    print("LOSE")