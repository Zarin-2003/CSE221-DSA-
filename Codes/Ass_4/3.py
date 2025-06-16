n=int(input())

mat=[[0]*n for i in range(n)]

for i in range(n):
    m=list(map(int,input().split()))
    for j in range(1,m[0]+1):
        mat[i][m[j]]=1
for i in mat:
    print(" ".join(map(str,i)))

