#Curse the Darkness
NumTestCases = int(input())
for i in range(NumTestCases):
    BookX, BookY = map(float, input().split(" "))
    NumCandles = int(input())
    CandleCount = 0
    for j in range(NumCandles):
        CandleX, CandleY = map(float, input().split(" "))
        Distance = float((((CandleX - BookX) ** 2) + ((CandleY - BookY) ** 2)) ** 0.5)
        if Distance <= 8:
            CandleCount += 1
    if CandleCount > 0:
        print("light a candle")
    else:
        print("curse the darkness")