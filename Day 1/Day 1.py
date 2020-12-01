import numpy as np
import timeit
NUMS = np.loadtxt("C:/Users/wukai/OneDrive - Universiteit Twente/Code/Python/AOC/Day 1/NUMS.txt", delimiter = ",")

t = timeit.Timer()

for i in range(0,len(NUMS)):
    for j in range(i,len(NUMS)):
        for k in range(j,len(NUMS)):
            if NUMS[i]+NUMS[j]+NUMS[k] == 2020:      
                print('Num 1 = ', int(NUMS[i]))
                print('Num 2 = ', int(NUMS[j]))
                print('Num 3 = ', int(NUMS[k]))
                print('sum = ',  int(NUMS[i]+NUMS[j]+NUMS[k]))
                print('product = ', int(NUMS[i]*NUMS[j]*NUMS[k]))

t =t.timeit()