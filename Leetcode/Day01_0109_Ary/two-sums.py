#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

nums = [1,2,3,4,5,1]
target =5

def twosums(nums,target):
    dicc={}
    for i in range(len(nums)):
        if target-nums[i] in dicc:
            return([i, dicc[target-nums[i]]])
        else:
            dicc[nums[i]]=i

print(twosums(nums,target))


