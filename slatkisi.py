#Slatkisi
CandyPrice, NumZeros = map(int, input().split(" "))
print(str(int(round(float(CandyPrice/(10 ** NumZeros))) * (10 ** NumZeros))))