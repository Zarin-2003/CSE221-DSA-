import heapq
n,m=map(int,input().split())
adj_list={i:[] for i in range(1,n+1)}
for  i in range(m):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

danger=[float('inf')]*(n+1)

Q=[(0,1)]
danger[1]=0

while Q:
    d,u=heapq.heappop(Q)
    for v,w in adj_list[u]:
        max_d=max(danger[u],w)
        if max_d<danger[v]:
            danger[v]=max_d
            heapq.heappush(Q,(max_d,v))
for i in range(1,n+1):
    if danger[i]==float('inf'):
        danger[i]=-1
print(" ".join(map(str,danger[1::])))
