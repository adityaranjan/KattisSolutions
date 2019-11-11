#Cetvrta
XPOINTS = []
YPOINTS = []
for i in range(3):
    Xpoint, Ypoint = map(str, input().split(" "))
    XPOINTS.append(Xpoint)
    YPOINTS.append(Ypoint)
for j in range(3):
    if XPOINTS.count(XPOINTS[j]) == 1:
        Xoutput = XPOINTS[j]
    if YPOINTS.count(YPOINTS[j]) == 1:
        Youtput = YPOINTS[j]
print(str(Xoutput) + " " + str(Youtput))