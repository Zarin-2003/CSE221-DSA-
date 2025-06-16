import sys
sys.setrecursionlimit(10**6)

def DFS(adj_list,colour,u,):
    colour[u]=1
    for v in adj_list[u]:
        if colour[v]==0:
            if DFS(adj_list,colour,v)=="YES":
               return "YES"
            # a=DFS(adj_list,colour,v)
            # return a
        if colour[v]==1:
            return "YES"
    colour[u]=2
    return "NO"

def initializing(adj_list,colour):
    for u in adj_list:
        if colour[u]==0:
            if DFS(adj_list,colour,u)=="YES":
                return "YES"
            # a=DFS(adj_list,colour,u)
            # return a
    # return "NO"
n,m=map(int,input().split())
adj_list={i: [] for i in range(1,n+1)}
for i in range(m):
    s,e=map(int,input().split())
    adj_list[s].append(e)
for i in adj_list:
    adj_list[i].sort()

colour={i:0 for i in range(1,n+1)}
ans=initializing(adj_list,colour)
print(ans)