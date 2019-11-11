#Beat the Spread!
NumTestCases = int(input())
for i in range(NumTestCases):
    s, d = map(int, input().split(" "))
    ScoreOne = int((s + d) / 2)
    ScoreTwo = int(s - ScoreOne)
    if (ScoreOne + ScoreTwo == s) and (abs(ScoreOne - ScoreTwo) == d) and ScoreOne >= 0 and ScoreTwo >= 0:
        print(str(max(ScoreOne, ScoreTwo)) + " " + str(min(ScoreOne, ScoreTwo)))
    else:
        print("impossible")