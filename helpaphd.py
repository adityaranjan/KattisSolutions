#Help a PhD candidate out!
NumTestCases = int(input())
for i in range(NumTestCases):
    Problem = input()
    if Problem == "P=NP":
        print("skipped")
    else:
        Num1, Num2 = map(int, Problem.split("+"))
        print(str(Num1 + Num2))