


# def rrr(a,n,m):
#     if n==1:
#         return a%m

#     half_n=n//2
#     half_sum=rrr(a,half_n,m)
#     pow_half=func_exponen(a,half_n,m)

#     if n%2==0:
#         return (half_sum*(1+pow_half))%m
#     else:
#         return (half_sum*(1+pow_half)+func_exponen(a,n,m))%m
    
t=int(input())
final=[]
for i in range(t):
    a,n,m=map(int,input().split())
    if a==1:
        final.append(str(n%m))
        continue
    aa=a
    nn=n+1
    mm=(a-1)*m
    res_val= 1
    while nn>0:
        if nn% 2 == 1:
            res_val= (res_val*aa) % mm
        aa= (aa*aa) % mm
        nn//= 2
    point=(res_val-a)%mm
    res=(point//(a-1))%m
    final.append(str(res))
print("\n".join(final))