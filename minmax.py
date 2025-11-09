import sys
def findminmax(nums,left,right,min=sys.maxsize,max=-sys.maxsize):
    if left==right:
        if min>nums[right]:
            min=nums[right]
        if max<nums[left]:
            max=nums[left]
        return min,max
    if right-left==1:
        if nums[left]<nums[right]:
            if min>nums[left]:
                min=nums[left]
            if max<nums[right]:
                max=nums[right]
            return min,max
        else:
            if min>nums[right]:
                min=nums[right]
            if max<nums[left]:
                max=nums[left]
            return min,max
    mid=(left+right) //2
    min,max=findminmax(nums,left,mid,min,max)
    min,max=findminmax(nums,mid+1,right,min,max)
    return min,max
if __name__=='__main__':
    nums=[8,9,4,6,2,3,1]
    (min,max)=findminmax(nums,0,len(nums)-1)
    print("min:",min)
    print("max:",max)

