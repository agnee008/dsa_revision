"""
Approach
Initialize an Empty Target Array: Start with an empty list to build the target array.
Insert Elements Based on Index: Iterate through the nums and index arrays. 
For each element, insert it at the specified position in the target array.
Handle Insertion: Python's list insert() method can be used to insert elements at specific indices.


"""

def createTargetArray(nums, index):
    target = []
    for num, idx in zip(nums, index):
        target.insert(idx, num)
    return target

# Example usage:
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(createTargetArray(nums, index))  # Output: [0, 4, 1, 3, 2]
