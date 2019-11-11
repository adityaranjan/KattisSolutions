#Recount
from collections import Counter
result = True
CandidateList = []
Winner = ""
while result == True:
    CandidateName = str(input())
    if CandidateName == "***":
        result = False
    else:
        CandidateList.append(CandidateName)
CountList = list(Counter(CandidateList).most_common(2))
if len(CountList) == 1:
    WinCandidate = CountList[0][0]
elif CountList[0][1] == CountList[1][1]:
    WinCandidate = "Runoff!"
else:
    WinCandidate = CountList[0][0]
print(WinCandidate)