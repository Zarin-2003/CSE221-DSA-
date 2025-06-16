n,m=map(int,input().split())

u=list(map(int,input().split()))
v=list(map(int,input().split()))

# mat=[[0]*n for i in range(1,n+1)]

# for i in range(m):
#     mat[u[i]-1][v[i]-1]=1

inn=[0]*n
out=[0]*n

for i in range(m):
    out[u[i]-1]+=1
    inn[v[i]-1]+=1

for i in range(n):
    print(inn[i]-out[i],end=" ")