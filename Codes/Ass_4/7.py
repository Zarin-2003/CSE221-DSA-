import math
n,m=map(int,input().split())
l={i:[] for i in range(1,n+1)}
for i in range (1,n+1):
    for j in range(1,n+1):
        if i!=j and math.gcd(i,j)==1:
            l[i].append(j)
    
for i in range(m):
    x,k=map(int,input().split())
    if k-1<len(l[x]):
      print(l[x][k-1])
    else:
        print("-1") 