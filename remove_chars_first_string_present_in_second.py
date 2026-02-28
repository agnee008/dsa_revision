def removeChars(str1: str, str2: str) -> str:
    # Create a set of characters present in the second string
    chars_to_remove = set(str2)
    
    # Use list comprehension to filter out the characters from str1 that are not in the set
    result = [char for char in str1 if char not in chars_to_remove]
    
    # Join the list back into a string
    return ''.join(result)

# Example usage:
str1 = "geeksforgeeks"
str2 = "mask"

print(removeChars(str1, str2))  # Output: "geeforgee"
