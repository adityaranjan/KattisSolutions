switch = input()
beforedelete = list(str(input()))
afterdelete = list(str(input()))
beforedeletelength = len(beforedelete)
afterdeletelength = len(afterdelete)
switchcheck = 0
for i in range(int(beforedeletelength)):
    if int(switch) % 2 == 0:
        if int(beforedelete[i]) == int(afterdelete[i]):
            switchcheck = int(switchcheck) + 1
    elif int(switch) % 2 != 0:
        if int(beforedelete[i]) == abs(int(afterdelete[i]) - 1):
            switchcheck = int(switchcheck) + 1
if int(switchcheck) == int(beforedeletelength):
    print("Deletion succeeded")
else:
    print("Deletion failed")