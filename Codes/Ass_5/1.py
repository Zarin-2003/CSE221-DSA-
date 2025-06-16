from collections import deque
n,m=map(int,input().split())
adj_list={i: [] for i in range(1,n+1)}
for i in range(m):
    s,e=map(int,input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

colour={i:0 for i in range(1,n+1)}  #visit er track rakhte
parent={i:None for i in range(1,n+1)}  #parent er track rakhte
Q=deque()
Q.append(1)
colour[1]=1
main=[]
while Q:
    u=Q.popleft() #shob kaj sesh. mane visit kora done, ekhon eke diye ashol kaj koro, pop kore variable rakhlam or children dhorte
    main.append(u) #ashol kaj
    for j in adj_list[u]:
        if colour[j]!=1:
            Q.append(j)
            colour[j]=1
print(" ".join(map(str,main))) 

#visit(colour) -> pop -> kaj -> children daka
