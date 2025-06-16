def merge(a, b):
    i,j=0,0
    c=0
    result=[]
    while i<len(a) and j<len(b):
        if int(a[i])<=int(b[j]):
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            c+=(len(a)-i)
            j+=1
    while i<len(a):
        result.append(a[i])
        i+=1
    while j<len(b):
        result.append(b[j])
        j+=1
    return (c,result)


def mergeSort(arr):
    if len(arr) <= 1:
        return 0,arr
    else:
        mid = len(arr)//2
        i1,a1 = mergeSort(arr[:mid]) 
        i2,a2 = mergeSort(arr[mid:])  
        i,a=merge(a1, a2)  
           
        return i+i1+i2,a
n=int(input())
arr=input().split()


inv,final=mergeSort(arr)


print(inv)
print(" ".join(final))

