def removeDuplicates(s: str, k: int) -> str:
    # Stack to keep track of characters and their counts
    stack = []
    
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c,1])
        if stack[-1][1] == k:
            stack.pop()
    res =""
    for char, count in stack:
        res += (char * count)
    return res
    
# Example usage:
print(removeDuplicates("abcd", 2))  # Output: "abcd"
print(removeDuplicates("deeedbbcccbdaa", 3))  # Output: "aa"
print(removeDuplicates("pbbcggttciiippooaais", 2))  # Output: "ps"
