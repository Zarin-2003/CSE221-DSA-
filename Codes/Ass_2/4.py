t=int(input())
for i in range(t):
    s=input()
    l=0
    r=len(s)-1
    found='-1'
    while l<=r:
        mid=(l+r)//2
        if s[mid]=='1':
            found=mid
            r=mid-1
        elif s[mid]=='0':
            l=mid+1
    if found=='-1':
        print(found)
    else:
        print(found+1)
