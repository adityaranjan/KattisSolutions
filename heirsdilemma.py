#Heir's Dilemma 

def isSelfDivisor(number):
    tempNum = number
    for j in range(6):
        if tempNum % 10 == 0 or number % (tempNum % 10) != 0:
            return False
        tempNum //= 10
    return True
    
L, H = map(int, input().split(" "))
count = 0
for i in range(L, H + 1, 1):
    if isSelfDivisor(i) and len(set(str(i))) == 6:
        count += 1
print(count)