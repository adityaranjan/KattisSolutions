#Ptice
AdrianAnswer = list("ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCA")
BrunoAnswer = list("BABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABC")
GoranAnswer = list("CCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAA")
AdrianCorrect = 0
BrunoCorrect = 0
GoranCorrect = 0
NumQuestions = int(input())
TestAnswers = list(input())
for i in range(NumQuestions):
    if TestAnswers[i] == AdrianAnswer[i]:
        AdrianCorrect += 1
    if TestAnswers[i] == BrunoAnswer[i]:
        BrunoCorrect += 1
    if TestAnswers[i] == GoranAnswer[i]:
        GoranCorrect += 1
PeopleCorrect = []
NumCorrect = max(AdrianCorrect, BrunoCorrect, GoranCorrect)
if AdrianCorrect == NumCorrect:
    PeopleCorrect.append("Adrian")
if BrunoCorrect == NumCorrect:
    PeopleCorrect.append("Bruno")
if GoranCorrect == NumCorrect:
    PeopleCorrect.append("Goran")
print(str(NumCorrect))
for j in range(len(PeopleCorrect)):
    print(PeopleCorrect[j])