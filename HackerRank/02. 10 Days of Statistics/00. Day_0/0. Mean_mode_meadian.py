# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats


ip = int(input())
num = list(map(int,input().split()))
print(np.mean(num))
print(np.median(num))
print(stats.mode(num)[0][0])

#num.sort()
#   # print('lol')
#print(round(sum(num)/len(num),1))  
#if len(num)%2==0 :
#    print(round((num[len(num)//2] + num[(len(num)//2)-1])/2,1))
#else :
#    print(round(num[len(num)//2],1))
#print(round(max(num,key=num.count),1)) 
