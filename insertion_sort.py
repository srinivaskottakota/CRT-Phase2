def performinsertion(nums):
    n=len(nums)
    lasteleinsortedarr=0
    for firstindex in range(1,n):
        temp=nums[firstindex]
        previous=lasteleinsortedarr
        while previous>=0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous=previous-1
            nums[previous+1]=temp
        nums[previous+1]=temp
        lasteleinsortedarr+=1
nums=list(map(int,input().split()))
print("Before sorting",nums)
performinsertion(nums)
print("after sorting",nums)