"""
Approach
Instead of using cmp_to_key, you can use a key function for sorting that directly creates a tuple of repeated concatenations. 
This way, Python's built-in sort can handle the comparisons correctly.

Convert Numbers to Strings: Convert each number to a string for easy concatenation.
Define a Custom Key for Sorting: Use a key function where each string is repeated enough times to ensure the correct order based on concatenation.
Sort the List: Sort the list of strings based on this key.
Join and Handle Leading Zeros: Join the sorted strings and handle cases where the result may start with zeros.
    
"""

from functools import cmp_to_key

def largestNumber(nums):
    for i, n in enumerate(nums):
        nums[i] = str(n)
        
    def compare(n1,n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
        
    nums = sorted(nums, key =cmp_to_key(compare))
    return "".join(nums)
    

# Example usage:
print(largestNumber([10, 2]))  # Output: "210"
print(largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"
print(largestNumber([0, 0]))  # Output: "0"
