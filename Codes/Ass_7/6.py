import heapq
n,m,s,d=map(int,input().split())
adj_list={i:[] for i in range(1,n+1)}
for  i in range(m):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
distance=[float('inf')]*(n+1)
distance2=[float('inf')]*(n+1)
Q=[(0,s)]
distance[s]=0

while  Q:
    w,u=heapq.heappop(Q)

    for  v,w2 in adj_list[u]:
        a=w+w2
        if  a<distance[v]:
            distance2[v]=distance[v]
            distance[v]=a
            heapq.heappush(Q,(a,v))
        elif distance[v]<a<distance2[v]:
            distance2[v]=a
            heapq.heappush(Q,(a,v))
if distance2[d]==float('inf'):
    print(-1)
else:
    print(distance2[d])          