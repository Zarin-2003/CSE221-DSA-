import heapq
def dijkstra_func(adj_list,distance,n,m,s,d):
    Q=[(0,s)]
    distance[s]=0
    while  Q:
        w,u=heapq.heappop(Q)
        if w>distance[u]:
            continue
        for  v,w2 in adj_list[u]:
            if  distance[u]+w2<distance[v]:
                distance[v]=distance[u]+w2
                heapq.heappush(Q,(distance[u]+w2,v))
                # parent[v]=u
    return distance
n,m,s,d=map(int,input().split())
adj_list1={i:[] for i in range(1,n+1)}

for  i in range(m):
    u,v,w=map(int,input().split())
    adj_list1[u].append((v,w))

distance1=[float('inf')]*(n+1)
distance2=[float('inf')]*(n+1)
# parent1={i:None for i in range(1,n+1)}
# parent2={i:None for i in range(1,n+1)}
d1=dijkstra_func(adj_list1,distance1,n,m,s,d)
d2=dijkstra_func(adj_list1,distance2,n,m,d,s)


max_t=float('inf')
ans_node=-1
for i in range(1,n+1):
    
    if d1[i]!=float('inf') and d2[i]!=float('inf'):
        meet_time=max(d1[i],d2[i])
        if meet_time<max_t or  (meet_time==max_t and i<ans_node):
            max_t=meet_time
            ans_node=i
if ans_node==-1:
    print(-1)
    exit()
print(f"{max_t}  {ans_node}")

