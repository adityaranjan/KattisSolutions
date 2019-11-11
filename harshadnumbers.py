#Harshad Numbers
N = int(input())
found = False
while found == False:
    if N % (sum(list(map(int, list(str(N)))))) == 0:
        print(N)
        found = True
    N += 1