n,m=map(int,input().split())

u=list(map(int,input().split()))
v=list(map(int,input().split()))

# mat=[[0]*n for i in range(1,n+1)]

# for i in range(m):
#     mat[u[i]-1][v[i]-1]=1
#     mat[v[i]-1][u[i]-1]=1
# c=0
# l=[]
# for i in range(n):
#     sum=0
#     for j in range(n):
#         if mat[i][j]!=0:
#             sum+=1
#     l.append(sum)
# for i in range(len(l)):
#     if l[i]%2!=0:
#         c+=1
# if c==2 or c==0:
#     print("YES")
# else:
#     print("NO")
l=[0]*n
c=0
for i in range(m):
    l[u[i]-1]+=1
    l[v[i]-1]+=1
for i in range(n):
    if l[i]%2!=0:
        c+=1
if c==2 or c==0:
    print("YES")
else:
    print("NO")
