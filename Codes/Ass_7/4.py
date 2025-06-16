import heapq
n,m,s,d=map(int,input().split())
w=[0]+list(map(int,input().split()))
adj_list={i:[] for i in range(1,n+1)}

for i  in range(m):
    u,v=map(int,input().split())
    adj_list[u].append(v)
distance=[float('inf')]*(n+1)
Q=[(w[s],s)]
distance[s]=w[s]

while Q:
    di,u=heapq.heappop(Q)
    for v in adj_list[u]:
        if distance[u]+w[v]<distance[v]:
            distance[v]=distance[u]+w[v]
            heapq.heappush(Q,(distance[v],v))
if distance[d]==float('inf'):
    print(-1)
else:
    print(distance[d])