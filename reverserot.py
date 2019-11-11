#Reverse Rot
import string
LettersList = list(string.ascii_uppercase)
LettersList.append("_")
LettersList.append(".")
while True:
    Line = input()
    if Line == "0":
        break
    else:
        EncryptedMessage = []
        Shift, OriginalMessage = Line.split(" ")
        OriginalMessage = list(OriginalMessage)
        OriginalMessage.reverse()
        i = 0
        for i in range(len(OriginalMessage)):
            if LettersList.index(OriginalMessage[i]) + int(Shift) > 27:
                EncryptedMessage.append(LettersList[(LettersList.index(OriginalMessage[i]) + int(Shift)) % 28])
            else:
                EncryptedMessage.append(LettersList[LettersList.index(OriginalMessage[i]) + int(Shift)])
        print(''.join(EncryptedMessage))