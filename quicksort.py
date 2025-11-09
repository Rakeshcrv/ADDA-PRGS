def particition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
def qs(arr,low,high):
    if low<high:
        pi=particition((arr),low,high)
        qs(arr,low,pi-1)
        qs(arr,pi+1,high)
if __name__=='__main__':
    arr=[84,8,6,98,23,56]
    n=len(arr)
    qs(arr,0,n-1)
    print("sorted array:")
    for x in arr:
        print(x,end=" ")