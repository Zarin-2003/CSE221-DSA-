n,m=map(int,input().split())
mat=[[0]*n for i in range(n)]
for i in range(m):
    u,v,w=map(int,input().split())
    mat[u-1][v-1]=w

for i in mat:
    print(" ".join(map(str,i)))