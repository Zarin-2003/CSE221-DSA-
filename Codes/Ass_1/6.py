#selection sort
n=int(input()) #please work
Si=input().split()
Sm=input().split()
swap=0

for i in range(n):
    Si[i]=int(Si[i])
    Sm[i]=int(Sm[i])

for i in range(n):
    max_i=i
    for j in range(i+1,n):
        if Sm[j]>Sm[max_i]:
            max_i=j
        elif Sm[j]==Sm[max_i] and Si[max_i]>Si[j]:
                max_i=j
    if max_i!=i:
         Si[i],Si[max_i]=Si[max_i],Si[i]
         Sm[i],Sm[max_i]=Sm[max_i],Sm[i]
         swap+=1
print(f"Minimum swaps: {swap}")
for i in range(n):
    print(f"ID: {Si[i]} Mark: {Sm[i]}")
