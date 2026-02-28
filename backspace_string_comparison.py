"""
Given two strings s and t, return true if they are equal when typed into empty text editors. 
x   Otherwise, return false. The # character means a backspace.

Approach
To solve this problem, we can simulate the typing process by using stacks.

Simulate the typing process: Use a stack to simulate the effect of typing each string, taking into account the backspace characters.
Compare the final results: After processing both strings, compare the final contents of the stacks.
Steps
Define a helper function: This function processes a string with backspaces and returns the final string after applying all backspaces.
Process both strings: Use the helper function to get the final versions of both strings.
Compare the results: Return true if the processed versions of both strings are equal, otherwise return false.

    
    
"""

def backspaceCompare(s: str, t: str) -> bool:
    def processString(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return processString(s) == processString(t)

# Example usage:
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))  # Output: True

s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t))  # Output: True

s = "a#c"
t = "b"
print(backspaceCompare(s, t))  # Output: False
