def lower_bound(n,arr,pair):
    l=0
    r=n-1
    x=int(pair[0])
    ans=n
    while l<=r:
        mid=(l+r)//2
        if (arr[mid])>=x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans
def upper_bound(n,arr,pair):
    l=0
    r=n-1
    x=int(pair[1])
    ans=n
    while l<=r:
        mid=(l+r)//2
        if (arr[mid])>x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

n,k=input().split()
n,k=int(n),int(k)
arr=input().split()
for i in range(n):
    arr[i]=int(arr[i])
final=[]
for i in range(k):
    pair=input().split()
    lower=lower_bound(n,arr,pair)
    upper=upper_bound(n,arr,pair)
    final.append(str(upper-lower))

print("\n".join(final))
