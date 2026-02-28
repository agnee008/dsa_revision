# Subarray producing the largest sum

def maxsubArray(nums:list[int]):
    maxsub = nums[0]
    cursum = 0

    for n in nums:
        if cursum < 0:
            cursum = 0
        cursum += n
        maxsub = max(maxsub,cursum)
    return maxsub

print(maxsubArray([-2,-3,4,-1,-2,1,5,-3]))


