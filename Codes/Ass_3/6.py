def post_order(inn,pre,l,r,result,inorder_map,root_pre=0):
    if l>r:
        return root_pre
    root=pre[root_pre]
    root_pre+=1
    root_ind=(inorder_map)[root]
    
    root_pre=post_order(inn,pre,l,root_ind-1,result,inorder_map,root_pre)
    root_pre=post_order(inn,pre,root_ind+1,r,result,inorder_map,root_pre)
    result.append(root)
    return root_pre
 
n=int(input()) 
inn = list(map(int, input().split()))
pre = list(map(int, input().split()))

inorder_map = {val: idx for idx, val in enumerate(inn)}
result=[]
post_order(inn,pre,0,n-1,result,inorder_map,0)
for i in range(n):
    result[i]=str(result[i])
print(" ".join(result))

