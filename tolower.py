#ToLower
P, T = map(int, input().split(" "))
ProblemCheck = 0
for i in range(P):
    TestCaseCheck = 0
    for j in range(T):
        word = input()
        if (word[0].isupper() and word[1:].islower()) or word.islower():
            TestCaseCheck += 1
    if TestCaseCheck == T:
        ProblemCheck += 1
print(str(ProblemCheck))