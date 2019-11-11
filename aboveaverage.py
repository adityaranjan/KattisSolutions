#Above Average
cases = int(input())
for a in range(cases):
    Class = list(map(int, input().split(" ")))
    NumStudents = len(Class) - 1
    Grades = []
    AboveAverage = []
    for i in range(NumStudents):
        Grades.append(Class[i + 1])
    AverageGrade = float(int(sum(list(Grades))) / int(Class[0]))
    for j in range(NumStudents):
        if Grades[j] > AverageGrade:
            AboveAverage.append(Grades[j])
    PercentAboveAverage = list(str(round(float((len(AboveAverage) / int(Class[0]) * 100)), 3)))
    if "." in PercentAboveAverage:
        ZerosList = ["0"] * (3 - len(PercentAboveAverage) + PercentAboveAverage.index(".") + 1)
        PercentAboveAverage += ZerosList
        print(str(''.join(PercentAboveAverage)) + "%")
    else:
        print(str(''.join(PercentAboveAverage)) + ".000%")