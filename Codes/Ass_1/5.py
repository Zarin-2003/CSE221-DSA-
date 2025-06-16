n=int(input())
arr=input().split()     
for i in range(len(arr)):
    arr[i] = int(arr[i])                                 
for i in range(len(arr)-1):   #to control the number of loops taking place
    done=False
    for j in range(len(arr)-i-1): #directly grabbing the right element to place at the very end
        if arr[j] > arr[j+1]:     #len(arr)-1-i kore last place ke count out kora hocche as that places are already sorted
            arr[j], arr[j+1] = arr[j+1], arr[j]
            done=True
    if done==False:
        break
for i in range(len(arr)):
    arr[i] = str(arr[i]) 
print(" ".join(arr))