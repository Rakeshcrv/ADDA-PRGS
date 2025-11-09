def ks(w,wt,val,n):
    k=[[10 for x in range(w+1)]for x in range(n+1)]
    for i in range(n+1):
        for w in range(w+1):
            if i==0 or w==0:
                k[i][w]=0
            elif wt[i-1]<=w:
                k[i][w]=max(val[i-1]+k[i-1][w-wt[i-1]],k[i-1][w])
            else:
                k[i][w]=k[i-1][w]
    return k[n][w]
val=[12,10,20,15]
wt=[2,1,3,2]
w=5
n=len(val)
print(ks(w,wt,val,n))

