n=int(input())
arr=input().split()
for i in range(n):
    arr[i]=int(arr[i])

curr_sum=0
max_sum=0
max_i=arr[0]

for i in range(n-1):
    max_i=max(max_i,arr[i])   
    curr_sum=max_i+arr[i+1] **2
    max_sum=max(curr_sum,max_sum)

print(max_sum)



