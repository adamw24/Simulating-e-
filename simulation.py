import math
import statistics
import random
import numpy as np
N = 1000000
data = np.zeros(N)
n = N
s = 0
tempCount = 0

while (n > 0):
    rand = random.random()
    s += rand
    # print(s)
    tempCount += 1
    if (s >1):
        # print(tempCount)
        n -=1
        data[n] = tempCount
        tempCount =0
        s = 0

avgCount = statistics.mean(data)
std = statistics.stdev(data)
print(avgCount)
print(std)
print(math.e)