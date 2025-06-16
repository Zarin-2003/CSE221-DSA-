def balanced_bt(arr,l,r,final):
    if l>r:
        return
    mid=(l+r)//2
    final.append(str(arr[mid]))
    balanced_bt(arr,l,mid-1,final)
    balanced_bt(arr,mid+1,r,final)
    return final
n=int(input())
arr=input().split()
for i in range(n):
    arr[i]=int(arr[i])
result=balanced_bt(arr,0,n-1,final=[])
print(" ".join(result))
