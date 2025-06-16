from collections import deque

def BFS(adj_list,s):
    l={i:-1 for i in adj_list}
    colour={i:0 for i in adj_list}
    Q=deque()
    Q.append(s)
    l[s]=0
    colour[s]=1
    while Q:
        u=Q.popleft()
        for v in adj_list[u]:
            if colour[v]==0:
                colour[v]=1
                Q.append(v)
                l[v]=l[u]+1
                
    return l
n=int(input())
adj_list={i:[] for i in range(1,n+1)}
for i in range(n-1):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

l1=BFS(adj_list,1)
n1=max(l1,key=lambda x:l1[x])


l2=BFS(adj_list,n1)
n2=max(l2,key=lambda x:l2[x])


print(l2[n2])
print(f"{n1} {n2}")


