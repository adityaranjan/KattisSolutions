#Shattered Cake
CakeWidth = int(input())
N = int(input())
Area = 0
for i in range(N):
    w, l = map(int, input().split(" "))
    Area += (w * l)
print(str(round(Area/CakeWidth)))