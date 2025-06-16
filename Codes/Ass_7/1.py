import heapq
n,m,s,d=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))

adj_list={i:[] for i in range(1,n+1)}

for i  in range(m):
    adj_list[u[i]].append((v[i],w[i]))

parent={i:None for i in range(1,n+1)}

distance=[float('inf')]*(n+1)
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
            parent[v]=u
if distance[d]==float('inf'):
    print(-1)
    exit()

path=[]
temp=d

while temp!=None:
    path.insert(0,temp)
    temp=parent[temp]
    
if  path[0]==s:
    print(distance[d])
    print("  ".join(map(str,path)))
else:
    print(-1)
