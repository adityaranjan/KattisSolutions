#Suspension Bridges
import math
e = math.e
d, s = map(int, input().split(" "))
a = d
while True:
    const1 = e ** (d / a)
    const2 = const1 ** 0.5
    const3 = -d / (a ** 2)
    original = ((((const1 + 1) / const2) - 2) * (a / 2)) - s
    if abs(original) < 0.00001:
        break
    derivative = (((const1 + 1) / (2 * const2)) - 1) + ((a / 2) * ((((const1 ** 1.5) * const3) - ((1 / (2 * const2)) * const1 * const3 * (const1 + 1))) / const1))
    a = a - (original / derivative)
    if abs(original + s) < 0.5:
        a = d / 400
const4 = d / (2 * a)
print(a * ((e ** const4) - (e ** -const4)))