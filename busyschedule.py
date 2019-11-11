#Busy Schedule
while True:
    Input = int(input())
    if Input == 0:
        break
    else:
        TimeScoreDict = {}
        RepeatDict = {}
        i = 0
        for i in range(Input):
            Score = 0
            TimeInput = input()
            if TimeInput in TimeScoreDict.values() and TimeInput not in RepeatDict.keys():
                RepeatDict[TimeInput] = 1
            elif TimeInput in TimeScoreDict.values():
                RepeatDict[TimeInput] += 1
            Time, AmPm = TimeInput.split(" ")
            Hour, Minute = map(int, Time.split(":"))
            if Hour != 12:
                Score += (Hour * 100)
            if AmPm == "a.m.":
                Score += 2000
            if AmPm == "p.m.":
                Score += 4000
            Score += Minute
            TimeScoreDict[Score] = TimeInput
        ScoreList = list(TimeScoreDict.keys())
        ScoreList.sort()
        j = 0
        for j in range(len(ScoreList)):
            CurrentTime = TimeScoreDict[ScoreList[j]]
            print(CurrentTime)
            if CurrentTime in RepeatDict.keys():
                k = 0
                for k in range(RepeatDict[CurrentTime]):
                    print(CurrentTime)
        print("")