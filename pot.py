#Pot
cases = int(input())
x = 0
for i in range(cases):
    number = str(input())
    length = int(len(list(number)) - 1)
    exponent = int(number[length:])
    newnumber = int(number[:length])
    x += newnumber ** exponent
print(str(x))