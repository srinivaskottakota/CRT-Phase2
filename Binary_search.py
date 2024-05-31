nums=[12,4,32,24,56,532]
target =24
nums= sorted(nums)
print(nums)
left = 0
right = len(nums)-1
flag = -1
while left <= right:
    mid = (left + right)//2
    if nums[mid]==target:
        flag = mid
        break
    elif nums[mid]>target:
        right = mid-1
    else:
        left = mid+1
if flag==-1:
    print("Target Not Found")
else:
    print("Target Found at index",flag)
