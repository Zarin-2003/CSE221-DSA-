def lower_bound(n,arr,x):
    l=0
    r=n-1    
    while l<=r:
        mid=(l+r)//2
        if x<=arr[mid]:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans
def upper_bound(n,arr,x):
    l=0
    r=n-1
    ans=n
    while l<=r:
        mid=(l+r)//2
        if (arr[mid])>x:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans
arr=[1,2,5,7,8,13,13,13,15,17]
low=lower_bound(len(arr),arr,13)
up=upper_bound(len(arr),arr,13)
ans=(low,up-low)
print(ans)
