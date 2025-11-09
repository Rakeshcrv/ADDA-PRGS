def ss(set,n,sum):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False
    if (set[n-1]>sum):
        return ss(set,n-1,sum)
    return ss(set,n-1,sum) or ss(set,n-1,sum-set[n-1])
set=[3,34,4,12,5,27]
sum=9
n=len(set)
if (ss(set,n,sum==True)):
    print("subset found in  given sum")
else:
    print("subset not found")