#Divide by 100...
N = list(input())
M = list(input())
NLength = len(N)
MLength = len(M)
ZeroCount = MLength - 1
if NLength >= MLength:
    N.insert(NLength - ZeroCount, ".")
    i = 0
    while True:
        if N[NLength - i] == ".":
            del N[NLength - i]
            break
        elif N[NLength - i] == "0":
            del N[NLength - i]
            i += 1
        else:
            break
else:
    TempList = ["0"] * (MLength - NLength)
    N = TempList + N
    N.insert(1, ".")
    i = NLength - MLength
    while True:
        if N[NLength - i] == ".":
            del N[NLength - i]
            break
        elif N[NLength - i] == "0":
            del N[NLength - i]
            i += 1
        else:
            break
print(''.join(N))