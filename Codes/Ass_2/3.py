
n, k = input().split() 
n,k=int(n),int(k)
arr = input().split()  
curr_sum = 0
max_len = 0
i = 0 

for j in range(n):  
    curr_sum += int(arr[j])    
    while curr_sum > k and i <= j:
        curr_sum -= int(arr[i])
        i += 1   
    max_len = max(max_len, j - i + 1)

print(max_len)
