"""
    Approach
Sort the list: Start by sorting the stones in descending order.
Simulate the smashing process: Continuously take the two heaviest stones, smash them, and insert the result back into the sorted list.
Re-sort the list: After each insertion, re-sort the list to maintain the order.
Continue until one or no stones are left.
Return the last stone or 0 if no stones are left.
    
"""

def lastStoneWeight(stones):
    # Sort the stones in descending order
    stones.sort(reverse=True)
    
    while len(stones) > 1:
        # Take the two heaviest stones
        first = stones.pop(0)
        second = stones.pop(0)
        
        # If they are not equal, insert the difference back into the list
        if first != second:
            new_stone = first - second
            # Insert the new stone in sorted order
            stones.append(new_stone)
            stones.sort(reverse=True)
    
    # If there are no stones left, return 0; otherwise return the last stone
    return stones[0] if stones else 0

# Example usage:
stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones)) 
