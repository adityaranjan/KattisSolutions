#Exam
FriendScore = int(input())
MyAnswers = list(input())
FriendAnswers = list(input())
Same = 0
Different = 0
for i in range(len(MyAnswers)):
    if MyAnswers[i] == FriendAnswers[i]:
        Same += 1
    else:
        Different += 1
if FriendScore <= Same:
    print(str(FriendScore + Different))
elif FriendScore > Same:
    print(str(Same + len(MyAnswers) - FriendScore))