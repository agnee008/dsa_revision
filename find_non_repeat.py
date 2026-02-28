def nonRepeatChar(nums:list[int]):
    """
    Find the first non-repeating element in a list of integers.

    Args:
    nums (list[int]): A list of integers to check for non-repeating elements.

    Returns:
    int: The first non-repeating element in the list. If all elements are repeating, returns None.
    """
    ht = {}

    for i in nums:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in nums:
        if ht[i] == 1:
            return i


nums = [4, 5, 4, 5, 3, 4, 5]
print(nonRepeatChar(nums)) 

def findNonRepeatIndex(nums: list[int]) -> int:
    ht = {}
    
    for index, value in enumerate(nums):
        if value in ht:
            ht[value][0] += 1
        else:
            ht[value] = [1, index]
    
    for value, (count, index) in ht.items():
        if count == 1:
            return index
    
    return -1