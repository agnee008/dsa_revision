def findLeaders(arr):
    n = len(arr)
    leaders = []
    
    # Start with the last element as the initial leader
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    # Traverse the array from the second last to the first element
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    # Since we collected leaders from right to left, reverse the list
    leaders.reverse()
    
    return leaders

# Example usage:
arr = [16, 17, 4, 3, 5, 2]
print(findLeaders(arr))  # Output: [17, 5, 2]
