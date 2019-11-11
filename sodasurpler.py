#Soda Surpler
e,f,c = map(int, input().split(" "))
NumEmptyBottles = e + f
NumSodas = 0
while NumEmptyBottles >= c:
    NumEmptyBottles -= (c - 1)
    NumSodas += 1
print(NumSodas)