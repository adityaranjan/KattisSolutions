#Heart Rate
NumCases = int(input())
for i in range(NumCases):
    b, p = input().split(" ")
    Min = (60 * (int(b) - 1)) / float(p)
    Mid = (60 * int(b)) / float(p)
    Max = (60 * (int(b) + 1)) / float(p)
    print(str(Min) + " " + str(Mid) + " " + str(Max))