"""
You are given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 5

Output: 4

Example 2:

Input: nums = [-1,0,2,4,6,8], target = 10

Output: 6

"""

def searchInsertedPosition(nums, target):
    l,r = 0, len(nums) -1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r= mid -1 
    return l