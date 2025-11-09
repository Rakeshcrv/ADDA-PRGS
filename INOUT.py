def find(al,n):
    _in=[0]*n
    out=[0]*n
    for i in range(0,len(al)):
        list=al[i]
        out[i]=len(list)
        for j in range(0,len(list)):
            _in[list[j]]+=1
    print("vertex\tIN\tOUT")
    for k in range(0,n):
        print(str(k)+"\t"+str(_in[k])+"\t"+str(out[k]))
if __name__=="__main__":
    al=[]
    al.append([1,2])
    al.append([3])
    al.append([0,5,6])
    al.append([1,4])
    al.append([2,3])
    al.append([4,6])
    al.append([5])
    n=len(al)
    find(al,n)