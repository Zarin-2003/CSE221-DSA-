from collections import deque
def topological_Sort(adj_list,inn,n):
    Q=deque() #lexicographically thakle queue er jaygay priority queue use
    for i in range(1,n+1):
        if inn[i]==0:
            Q.append(i)
    main=[]
    while Q:
        u=Q.popleft()
        main.append(u)
        for i in adj_list[u]:
            inn[i]-=1
            if inn[i]==0:
                Q.append(i)
    return main

n,m=map(int,input().split())
adj_list={i: [] for i in range(1,n+1)}
inn={i:0 for i in range(1,n+1)}
for i in range(m):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    inn[b]+=1
ans=topological_Sort(adj_list,inn,n)
if ans==[] or len(ans)!=n:
    print(-1)
    exit()
print(" ".join(map(str,ans)))