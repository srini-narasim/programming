#Given a sorted array nums, remove the duplicates in-place
#such that each element appear only once and return the new length.

def removeDuplicates(nums):
    for i in range(len(nums) -1,0,-1):
        if nums[i] == nums[i-1]:
            del nums[i]
