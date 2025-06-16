n=int(input()) 
main=[]
for i in range(n):
    a=input().split()
    main+=[a]
    
# for i in range(n):
#     max_i=i
#     for j in range(i+1,n):
#         if main[j][0]<main[max_i][0]:
#             max_i=j
#         elif main[j][0]==main[max_i][0] and main[j][6]>main[max_i][6]:
#             max_i=j
#     if max_i!=i:
#         main[i],main[max_i]=main[max_i],main[i]

# for i in range(n):
#     print(" ".join(main[i]))

for i in range(n-1):
    for j in range(n-1-i):
        if main[j][0]>main[j+1][0]:
            main[j],main[j+1]=main[j+1],main[j]
        elif main[j][0]==main[j+1][0] and main[j][6]<main[j+1][6]:
            main[j],main[j+1]=main[j+1],main[j]
for i in range(n):
    print(" ".join(main[i]))


