bobage , bobretire , bobsave , aliceage , alicesave = map(int, input().split(" "))
bobmoney = bobsave * (bobretire - bobage)
i = aliceage
alicemoney = 0
while alicemoney <= bobmoney:
    alicemoney = alicesave * (int(i) - aliceage)
    i += 1
print(int(i - 1))