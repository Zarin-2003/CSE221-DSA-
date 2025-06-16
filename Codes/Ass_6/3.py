
from collections import deque
move=[(-2,-1),(-2, 1),(-1, -2), (-1, 2),(1, -2), (1, 2),(2, -1),(2, 1)]
n=int(input())

x1,y1,x2,y2=map(int,input().split())
# if not (1 <= x1 <= n and 1 <= y1 <= n and 1 <= x2 <= n and 1 <= y2 <= n):
#     print(-1)
#     exit()
# if x1 == x2 and y1 == y2:
#     print(0)
#     exit()

visited =[]

Q=deque()
Q.append((x1,y1,0))
visited.append((x1, y1))
while Q:
    x,y,d=Q.popleft()
    if x==x2 and y==y2:
        print(d)
        exit()
    for i in move:
        xx,yy=x+i[0],y+i[1]
        if 1<=xx<=n and 1<=yy<=n and (xx,yy) not in visited:
            
            Q.append((xx,yy,d+1))
            visited.append((xx,yy))
print(-1)

