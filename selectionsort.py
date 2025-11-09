def ss(array,size):
    for ind in range(size):
        min_idx=ind
        for j in range(ind+1,size):
            if array[j]<array[min_idx]:
                min_idx=j
        array[ind],array[min_idx]=array[min_idx],array[ind]
array=[56,87,34,56,12]
n=len(array)
ss(array,n)
print("the sorted array is:")
print(array)