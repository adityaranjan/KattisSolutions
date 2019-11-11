#ICPCAwards
NumTeams = int(input())
UniversityList = []
TeamCount = 0
for i in range(NumTeams):
    UniversityName, TeamName = input().split(" ")
    if UniversityList.count(UniversityName) != 1 and TeamCount <= 11:
        TeamCount += 1
        UniversityList.append(UniversityName)
        print(UniversityName + " " + TeamName)