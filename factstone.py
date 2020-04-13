#Factstone Benchmark
import math
while True:
    year = int(input())
    if year == 0:
        break
    else:
        logIntSize = (4 * (2 ** ((year - 1960) // 10))) * math.log(2)
        i = 5
        while True:
            if math.lgamma(i) > logIntSize:
                print(i - 2)
                break
            i += 1