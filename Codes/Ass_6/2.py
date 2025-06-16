#bipartite
from collections import deque
n,m=map(int,input().split())
adj_list={i:[] for i in range(1,n+1)}
for i in range(m):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

colour={i:-1 for i in range(1,n+1)}
max_num=0
for i in range(1,n+1):  #even  if its bfs,  still making sure every  node is visited
    if colour[i]==-1:
        Q=deque()
        Q.append(i)
        colour[i]=0
        count=[1,0] 
        while Q:
            u=Q.popleft()
            
            for v in adj_list[u]:
                if colour[v]==-1:
                    Q.append(v)
                    colour[v]=1-colour[u]
                    count[colour[v]]+=1
                elif colour[v]==colour[u]:
                    print(-1)
                    exit()
        max_num+=max(count) #jodi  disconnected  graph hoy,  shob gula component er  max ta nibo

print(max_num)
