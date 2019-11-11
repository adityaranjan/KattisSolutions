#Veci
from collections import Counter
x = int(input())
counter = x + 1
result = False
while result == False:
    if Counter(list(str(counter))) == Counter(list(str(x))):
        result = True
        print(str(counter))
    elif len(str(counter)) > len(str(x)):
        result = True
        print("0")
    counter += 1