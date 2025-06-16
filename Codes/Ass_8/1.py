n,k=map(int,input().split())
size={i:1 for i in range(1,n+1)}
parent={i:i for i in range(1,n+1)}

def find_parent(u):
    if parent[u]!=u:
        parent[u]=find_parent(parent[u])
    return parent[u]
def union(u,v):
    ulp_u=find_parent(u)
    ulp_v=find_parent(v)

    if ulp_u!=ulp_v:
        if size[ulp_u]<size[ulp_v]:
            parent[ulp_u]=ulp_v
            size[ulp_v]+=size[ulp_u]
            return size[ulp_v]
        else:
            parent[ulp_v]=ulp_u
            size[ulp_u]+=size[ulp_v]
            return size[ulp_u]
    else:
        return size[ulp_u]
for i in range(k):
    u,v=map(int,input().split())
    ans=union(u,v)
    print(ans)
