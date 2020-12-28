# Calculating weighted mean
# Day_0
ip = int(input())
dis = list(map(int,input().split()))
weg = list(map(int,input().split()))

  
num = sum([dis[i]*weg[i] for i in range(len(dis))])
den = sum(weg)
    
print(round(num/den,1))
