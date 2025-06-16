from collections import deque

n,m,s,d=map(int,input().split())
if s==d:
    print(0)
    print(s)
    exit()
adj_list={i: [] for i in range(1,n+1)}
one=list(map(int,input().split()))
two=list(map(int,input().split()))

for i in range(m):
    adj_list[one[i]].append(two[i])
    adj_list[two[i]].append(one[i])
for i in adj_list:
    adj_list[i].sort()


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
main.insert(0,temp)
while temp!=None:
    temp=parent[temp]
    if temp==None:
        break
    main.insert(0,temp)
if len(main)==1:
    print(-1)

else:
    print(len(main)-1)
    print(" ".join(map(str,main)))
