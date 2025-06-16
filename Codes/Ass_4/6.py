l=[]
n=int(input())
x,y=map(int,input().split())
c=0

if 1<=x-1<=n and 1<=y-1<=n:
    l.append((x-1,y-1))
    c+=1
if 1<=x-1<=n :
    l.append((x-1,y))
    c+=1
if 1<=x-1<=n and 1<=y+1<=n:
    l.append((x-1,y+1))
    c+=1
if  1<=y-1<=n:
    l.append((x,y-1))
    c+=1
if  1<=y+1<=n:
    l.append((x,y+1))
    c+=1
if 1<=x+1<=n and 1<=y-1<=n:
    l.append((x+1,y-1))
    c+=1
if 1<=x+1<=n :
    l.append((x+1,y))
    c+=1
if 1<=x+1<=n and 1<=y+1<=n:
    l.append((x+1,y+1))
    c+=1

print(c)

for i in l:
    
    print(" ".join(map(str,i)))