nums = [2,5,43,21,56]
target = int(input("Enter num:"))
flag = -1
n = len(nums)
for i in range(n):
    if nums[i] == target:
        flag = i
        break 
if flag == -1:
    print("Not Found")
else:
    print("Target Found at ",flag)