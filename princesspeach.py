#Saving Princess Peach
N, Y = map(int, input().split(" "))
ObstaclesFound = []
for i in range(Y):
    Obstacle = input()
    if Obstacle not in ObstaclesFound:
        ObstaclesFound.append(Obstacle)
for j in range(N):
    if str(j) not in ObstaclesFound:
        print(j)
print("Mario got " + str(len(ObstaclesFound)) + " of the dangerous obstacles.")