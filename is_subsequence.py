# Recursive Python program to check
# if a string is subsequence
# of another string

# Returns true if str1[] is a
# subsequence of str2[].

def isSubsequence(string1,string2):
    m = len(string1)
    n = len(string2)
    
    if string1[m-1] == string2[n-1]:
        return isSubsequence(string1[:-1], string2[:-1])
    
    # If the last characters don't match
    # Check if string1 can be a subsequence of string2 without the last character 
    return isSubsequence(string1, string2[:-1])

