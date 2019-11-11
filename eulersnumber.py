#Euler's Number
n = int(input())
e = 0
Product = 1
for i in range(n):
    Product = Product * (i + 1)
    e += (1/Product)
print(float(e + 1))