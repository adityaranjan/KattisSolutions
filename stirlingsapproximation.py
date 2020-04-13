#Stirling's Approximation
import math
import sys

log2plusPi= math.log(2) + math.log(math.pi)
logE = math.log(math.e)

for line in sys.stdin:
	n = int(line)
	if n != 0:
		logN = math.log(n)
		print(str(math.e ** (math.lgamma(n + 1) - ((0.5 * (log2plusPi + logN)) + (n * (logN - logE))))))
	else:
		break
#SOLVED