import random as rd 
import time
import numpy as np

#Basic
#Q1 print 5 random numbers
print([rd.random() for i in range(5)]) 

#Q2 generate N randon numbers between 1 & -1
def genN(n):
    numbers = [rd.uniform(-1,1) for i in range(n)]
    return numbers
#Given known N-value    
N = [10**i for i in range(1,5+1)]

#Advanced 1 show process time
for i in N:
    start = time.time()
    a = genN(i)
    end = time.time()
    print("N = ",i)
    print("start time:{:5f}s".format(start))
    print("end time:",end)
    print("during time:{:5f}s".format(end-start))
    print("avg.:",np.mean(a))
    print("std.:",np.std(a))
"""
[0.2312326384833029, 0.9692119309112468, 0.1325347739828472, 0.3773255888769439, 0.355121303237497]
N =  10
start time:1493681954.339128s
end time: 1493681954.3411276
during time:0.002000s
avg: -0.159474877546
std: 0.494042833585
N =  100
start time:1493681954.342128s
end time: 1493681954.3421278
during time:0.000000s
avg: 0.0177888082119
std: 0.551741075029
N =  1000
start time:1493681954.342128s
end time: 1493681954.344128
during time:0.002000s
avg: -0.0134309401672
std: 0.581237207156
N =  10000
start time:1493681954.345128s
end time: 1493681954.3601289
during time:0.015001s
avg: -0.00729224681101
std: 0.573699647621
N =  100000
start time:1493681954.362129s
end time: 1493681954.4311328
during time:0.069004s
avg: -0.00320079360239
std: 0.578012904088
"""
