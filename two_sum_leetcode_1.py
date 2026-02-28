"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

# NOTE: Method -1 (Brute Force)

def twoSum_m1(nums:list[int], target:int) -> list:
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []


# Method -2 : Most Optimum 

def twoSum_m2(nums:list[int], target:int) -> list:
    num_availaible = {}
    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in num_availaible:
            return [i, num_availaible[required_num]]
        else:
            num_availaible[nums[i]] = i
    return []



if __name__=="__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum_m2(nums,target))