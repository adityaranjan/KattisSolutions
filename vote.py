#Popular Vote
Cases = int(input())
Votes = []
for a in range(Cases):
    NumCandidates = int(input())
    for b in range(NumCandidates):
        Votes.append(int(input()))
    MaxVotes = max(Votes)
    MaxVoteRepeat = 0
    for c in range(NumCandidates):
        if MaxVotes == Votes[c]:
            MaxVoteRepeat += 1
    if MaxVoteRepeat > 1:
        print("no winner")
    elif MaxVotes > float(int(sum(Votes)) / 2):
        print("majority winner " + str((Votes.index(max(Votes)) + 1)))
    else:
        print("minority winner " + str((Votes.index(max(Votes)) + 1)))
    for d in range(NumCandidates):
        del Votes[0]