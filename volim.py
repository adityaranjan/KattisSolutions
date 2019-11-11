#Volim
PlayerNum = int(input())
NumQuestions = int(input())
Timer = 0
for i in range(NumQuestions):
    TimeAdd, Response = input().split(" ")
    Timer += int(TimeAdd)
    if Timer >= 210:
        print(PlayerNum)
        break
    if Response == "T" and PlayerNum != 8:
        PlayerNum += 1
    elif Response == "T" and PlayerNum == 8:
        PlayerNum = 1