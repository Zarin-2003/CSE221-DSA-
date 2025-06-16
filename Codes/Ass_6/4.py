import sys
sys.setrecursionlimit(10**6)

def DFS(u):
    colour[u]=1
    curr=1
    for v in adj_list[u]:
        if colour[v]==0:
            curr+=DFS(v)
    colour[u]=2
    sub[u]=curr
    return curr

n,r=map(int,input().split())
adj_list=[[] for _ in range(n + 1)]
for i in range(n-1):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
colour=[0]*(n+1)
sub=[-1]*(n+1)
DFS(r)
q=int(input())
for i in range(q):
    b=int(input())
    print(sub[b])