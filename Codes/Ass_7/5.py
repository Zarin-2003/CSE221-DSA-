import heapq
n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))

adj_list={i:[] for i in range(1,n+1)}

for i  in range(m):
    adj_list[u[i]].append((v[i],w[i]))

distance=[[float('inf')] * 2 for _ in range(n + 1)]
Q=[(0,1,-1)]
distance[1][0]=0
distance[1][1]=0

while Q:
    d,u,checker=heapq.heappop(Q)
    for v,w in adj_list[u]:
        curr=w%2
        if curr==checker:
            continue
       
        if d+w<distance[v][curr]:
                distance[v][curr]=d+w
                heapq.heappush(Q,(d+w,v,curr))


ans = min(distance[n])
print(ans if ans != float('inf') else -1)