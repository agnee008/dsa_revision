def smallestPositive(nums):
    numSet = set(nums)
    
    smallest = 1
    while smallest in numSet:
        smallest += 1
    return smallest