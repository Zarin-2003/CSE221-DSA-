n,m=map(int,input().split())

u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
#
adj_list={i: [] for i in range(1,n+1)}

for i in range(m):
    adj_list[u[i]].append((v[i],w[i]))

for i in range(1, n + 1):
    print(f"{i}:", end=" ")#
    print(" ".join(f"({x},{y})" for x, y in adj_list[i]))

