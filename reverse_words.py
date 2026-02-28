def reverseWords(s: str) -> str:
    # Step 1: Strip leading and trailing spaces and split the string into words
    words = s.strip().split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join the reversed list of words with a single space
    return ' '.join(reversed_words)

# Example usage:
s1 = "the sky is blue"
print(reverseWords(s1))  # Output: "blue is sky the"

s2 = "  hello world  "
print(reverseWords(s2))  # Output: "world hello"

s3 = "a good   example"
print(reverseWords(s3))  # Output: "example good a"
