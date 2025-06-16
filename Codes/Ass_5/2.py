import sys
sys.setrecursionlimit(10**6)

def DFS(adj_list,colour,u,main):
    colour[u]=1  #visit,grey
    main.append(u)    #kaj  hobe  grey bananor time e
    t+=1
    discovery[u]=t
    for v in adj_list[u]:
        if colour[v]==0:
            DFS(adj_list,colour,v,main)
    colour[u]=2
    t+=1
    finish[u]=t


def initializing(adj_list,colour,main):
    t=0
    for u in adj_list:
        if colour[u]==0:
            DFS(adj_list,colour,u,main)


n,m=map(int,input().split())
f=list(map(int,input().split()))
t=list(map(int,input().split()))     
adj_list={i: [] for i in range(1,n+1)}
for i in range(m):
    adj_list[f[i]].append(t[i])
    adj_list[t[i]].append(f[i])
for i in adj_list:
    adj_list[i].sort()
colour={i:0 for i in range(1,n+1)}
discovery={i:0 for i in range(1,n+1)}
finish={i:0 for i in range(1,n+1)}
main=[]
total=initializing(adj_list,colour,main)
print(" ".join(map(str,main)))