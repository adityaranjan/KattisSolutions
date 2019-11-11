#Words For Numbers
import sys
Ones = {0: "zero", 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
Special = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
Tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
for line in sys.stdin:
    LINE = line.rstrip('\n')
    WordsList = list(LINE.split(" "))
    OutputList = []
    i = 0
    for i in range(len(WordsList)):
        if WordsList[i].isnumeric():
            if int(WordsList[i]) in Special.keys():
                OutputList.append(str(Special[int(WordsList[i])]))
            if int(WordsList[i]) < 10:
                OutputList.append(str(Ones[int(WordsList[i])]))
            if int(WordsList[i]) > 19:
                if int(WordsList[i]) % 10 == 0:
                    OutputList.append(str(Tens[int(WordsList[i]) // 10]))
                else:
                    OutputList.append(str(Tens[int(WordsList[i]) // 10]) + "-" + str(Ones[int(WordsList[i]) % 10]))
            if i == 0:
                LIST = list(OutputList[i])
                LIST[0] = LIST[0].upper()
                OutputList[i] = ''.join(LIST)
        else:
            OutputList.append(WordsList[i])
    print(' '.join(OutputList))