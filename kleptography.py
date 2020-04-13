import string
import math

AlphaDict = {}
for a in range(26):
    AlphaDict[string.ascii_lowercase[a]] = a
lenKey, lenText = map(int, input().split(" "))
key = input()
encryptText = input()
plainText = key[len(key) :: -1]
for i in range(lenText // lenKey):
    tempKey = ""
    for j in range(lenKey, 0, -1):
        decryptLetter = string.ascii_lowercase[(AlphaDict[encryptText[(-i * lenKey) - 1 - lenKey + j]] - AlphaDict[key[j - 1]]) % 26]
        plainText += decryptLetter
        tempKey += decryptLetter
    key = tempKey[len(tempKey) :: -1]
plainText = plainText[len(plainText) :: -1]
plainText = plainText[(lenKey - (lenText % lenKey)) : len(plainText)]
print(plainText)