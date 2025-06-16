
import heapq
def topological_Sort(adj_list,inn):
    Q=[] #lexicographically thakle queue er jaygay priority queue use
    for i in inn.keys():
        if inn[i]==0:
            heapq.heappush(Q,i)
    main=[]
    while Q:
        u=heapq.heappop(Q)
        main.append(u)
        for i in adj_list[u]:
            inn[i]-=1
            if inn[i]==0:
                heapq.heappush(Q,i)
    return main    
n=int(input())
l=[]
adj_list={}
all_char=set()
for i in range(n):
    a=input()
    l.append(a)
    all_char.update(a)
for i in all_char:
    adj_list[i]=[]
inn={i:0 for i in adj_list.keys()}
for i in range(n-1):
    a=l[i]
    b=l[i+1]
    for j in range(min(len(a),len(b))):
        if a[j]!=b[j]:
            if b[j] not in adj_list[a[j]]:
                adj_list[a[j]].append(b[j])
                inn[b[j]]+=1
            break
    else:
        if len(a)>len(b):
            print(-1)
            exit()

ans=topological_Sort(adj_list,inn.copy())
if len(ans)!=len(all_char):
    print(-1)
else:
    print("".join(ans))
