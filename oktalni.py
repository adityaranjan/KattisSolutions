#Oktalni
BinaryNumber = int(input(), 2)
OctalNumberList = list(oct(BinaryNumber))
for i in range(2):
    del OctalNumberList[0]
OctalNumber = ""
for j in range(int(len(OctalNumberList))):
    OctalNumber = OctalNumber + str(OctalNumberList[j])
print(str(OctalNumber))