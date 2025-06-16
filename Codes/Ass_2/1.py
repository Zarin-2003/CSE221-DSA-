n,s=input().split()
n,s=int(n),int(s)
curr_sum=0
arr=input().split()
for i in range(n):
    arr[i]=int(arr[i])
 
i=0
j=n-1
flag=False  
while(i<j):
    if arr[i]+arr[j]==s:
        print(i+1,j+1)
        flag=True
        break
    elif s<arr[i]+arr[j]:
        j-=1
    elif s>arr[i]+arr[j]:
        i+=1
if flag==False:
    print("-1") 