from collections import deque
def BFS_path(s,d,n,adj_list):
    Q=deque()
    Q.append(s)

    colour={i:0 for i in range(1,n+1)}  #visit er track rakhte
    parent={i:None for i in range(1,n+1)} 
    distance={i:0 for i in range(1,n+1)}
    colour[s]=1
    curr_dis=0
    while Q:
        u=Q.popleft()
        if u==d:
            break
        for j in adj_list[u]:
            if colour[j]!=1:
                Q.append(j)
                colour[j]=1
                parent[j]=u
    main=[]
    temp=d
    
    while temp!=None:
        main.insert(0,temp)
        temp=parent[temp]
        
    if not main or main[0]!=s:
        return []
    return main



n,m,s,d,k=map(int,input().split())

adj_list={i: [] for i in range(1,n+1)}
for i in range(m):
    one,two=map(int,input().split())
    adj_list[one].append(two)
    
for i in adj_list:
    adj_list[i].sort()



if s==k:
    path1 = [s]
else:
    path1 = BFS_path(s, k, n, adj_list)

if k == d:
    path2 = [k]
else:
    path2 = BFS_path(k, d, n, adj_list)

if not path1 or not path2:
    print(-1)
else:
    total=path1+path2[1:]
    print(len(total)-1)
    print(" ".join(map(str,total)))
