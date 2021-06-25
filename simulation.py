import math
import statistics
import random
import numpy as np

numTrials = 100000

def printResults(data):
    avgCount = statistics.mean(data)
    std = statistics.stdev(data)
    print(" e approx:", round(avgCount,4), " actual:", round(math.e,4))
    print(" std dev:", round(std,4))
    print(" 95% confidence interval: (", round(avgCount - std/np.sqrt(numTrials),4), ",", round(avgCount + std/np.sqrt(numTrials),4), ")\n" )
    return std


# Initial simulation: straightforward but requires many trials (N) to decrease variance 
print("\nSimulation 1: Initial/Straightforward")

data1 = np.zeros(numTrials)
n = numTrials
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
        data1[n] = tempCount
        tempCount =0
        s = 0

std1 = printResults(data1)



#Improved simulation that reduces variance by using antithetic variables    

print("Simulation 2: using anithetic variables to reduce variance")
data2 = np.zeros(numTrials)
n = numTrials
s1, s2 = 0, 0  
N1, N2 = 0, 0
N1Less1, N2Less1 = True, True
while (n > 0):
    u1 = random.random()
    s1 += u1
    u2 = 1-u1
    s2 += u2

    if(N1Less1):
        N1 += 1
    if(N2Less1):
        N2 += 1
    if (s1 >1 and s2>1):
        n -=1
        data2[n] = (N1 + N2)/2.0
        s1, s2 = 0, 0 
        N1, N2 = 0, 0
        N1Less1, N2Less1 = True, True
    elif(s1 > 1):
        N1Less1 = False
    elif(s2 > 1):
        N2Less1 = False

std2 = printResults(data2)


#Calculate improved efficiency
# 2e-2 observations per simulation for the improved version compared to 
# e observations per simulation for the original
obs2 = round((2*math.e -2)/math.e,4)
obs1 = round((std1/std2)**2,4)
print("Calculating improved efficiency: ")
print("",obs2, "times as many observations for Simulation 2, (2e-2), compared to Simulation 1 (e).")
print(" Would need", obs1, "times as many observations for Simulation 1 to have same variance as Simulation 2.")
print(" Simulation 2 is", obs1,"/",obs2,"=", round(obs1/obs2,4), "times as efficient as Simulation 1.\n" )