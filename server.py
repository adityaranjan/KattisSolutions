#Server
NumTasks, TimeLimit = map(int, input().split(" "))
TasksList = list(map(int, input().split(" ")))
TimeTaken = 0
TasksCompleted = 0
for i in range(NumTasks):
    if TimeTaken < TimeLimit and TasksList[i] + TimeTaken <= TimeLimit:
        TimeTaken += TasksList[i]
        TasksCompleted += 1
    else:
        break
print(str(TasksCompleted))