from collections import deque
r,c=map(int,input().split())
adj_list={i:[] for i in range(r*c)}
visited=[0]*(r*c)
val={i:'' for i in range(r*c)}
m=0
for i in range(r):
    a=input().strip()
    for j in a:
        val[m]=j
        m+=1
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=1
    d=0
    if val[start]=='D':
        d+=1

    while q:
        node = q.popleft()
        x,y=divmod(node,c)
        for i,j in dirs:
            xi,yj=x+i,y+j
            if 0<=xi<r and 0<=yj<c:
                adj=xi*c+yj
                if not visited[adj] and val[adj]!="#":
                    visited[adj]=1
                    if val[adj]=='D':
                        d+=1
                    q.append(adj)
    return d


max_d=0
for i in range(r*c):
    if not visited[i] and val[i]!='#':
        count=bfs(i)
        max_d=max(max_d,count)

print(max_d)


