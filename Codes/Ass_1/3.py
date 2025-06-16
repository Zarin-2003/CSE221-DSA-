n,k=input().split()
n=int(n)
k=int(k)
arr=input().split()
for i in range(n):
    arr[i]=int(arr[i])
    
arr=arr[::-1]
result=[]
for i in range(n-k,n):
   result+=[str(arr[i])]
print(" ".join(result))
   
   
    
