costofseed = input()
numberoflawns = input()
sizestore = [None] * int(numberoflawns)
for i in range(int(numberoflawns)):
    x = input()
    xone,xtwo = x.split(" ")
    sizestore[i] = float(xone) * float(xtwo)
    
totalsize = 0
i = 0
for i in range(int(numberoflawns)):
    totalsize = float(totalsize) + sizestore[i]
    
totalcost = float(totalsize) * float(costofseed)
print(float(totalcost))