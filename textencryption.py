#Text Encryption
while True:
    n = int(input())
    if n == 0:
        break
    else:
        charList = list(''.join(input().upper().split(" ")))
        cipherList = [None for i in range(len(charList))]
        overCount, j = 0, 0
        for i in range(len(charList)):
            if j > len(charList) - 1:
                overCount += 1
                j = overCount
            cipherList[j] = charList[i]
            j += n
        print(''.join(cipherList))