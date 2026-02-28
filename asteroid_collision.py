"""
You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [2,4,-4,-1]

Output: [2]

Example 2:

Input: asteroids = [5,5]

Output: [5,5]

Example 3:

Input: asteroids = [7,-3,9]

Output: [7,9]

"""
from typing import List
def asteroid_collision(asteroids: List[int]):
    stack = []
    for a in asteroids:
        stack.append(a)
        while len(stack) >=2 and stack[-1] < 0 and stack[-2] > 0:
            first = stack.pop()
            second = stack.pop()
            if abs(first) < abs(second):
                stack.append(second)
            elif abs(second) < abs(first):
                stack.append(first)
    return stack
                
                
        
        
    