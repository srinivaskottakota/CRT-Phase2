def performBubblesort(nums):
    n = len(nums)
    fixthisindex = n-1
    while fixthisindex > 0:
        for index in range(fixthisindex):
            for index in range(fixthisindex):
                if nums[index]>nums[index+1]:
                    temp=nums[index]
                    nums[index]=nums[index+1]
                    nums[index+1]=temp
            print(nums)
            fixthisindex -= 1
nums=[10,2,45,4,40,18,90,31]
print("Before sorting",nums)
performBubblesort(nums)
print("after sorting",nums)