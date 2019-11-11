#Polynomial Multiplication 1
NumTestCases = int(input())
for i in range(NumTestCases):
    FirstDegree = int(input())
    FirstCoefficients = list(map(int, input().split(" ")))
    SecondDegree = int(input())
    SecondCoefficients = list(map(int, input().split(" ")))
    OutputCoefficients = [0] * (FirstDegree + SecondDegree + 1)
    j = 0
    for j in range(len(FirstCoefficients)):
        k = 0
        for k in range(len(SecondCoefficients)):
            OutputCoefficients[j + k] += FirstCoefficients[j] * SecondCoefficients[k]
    print(str(FirstDegree + SecondDegree))
    print(' '.join(map(str, OutputCoefficients)))