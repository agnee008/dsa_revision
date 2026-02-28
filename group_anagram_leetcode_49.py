"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def grouAnagram(strs: list[str]) -> list[list[str]]:
    if len(strs) == 0:
        raise ValueError("Input cannot be blank") 
    reversed_string = [''.join(sorted(i)) for i in strs]
    hash={}
    for i in range(len(reversed_string)):
        if reversed_string[i] in hash:
            hash[reversed_string[i]].append(strs[i])
        else:
            hash[reversed_string[i]] = [strs[i]]
    return list(hash.values())

if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(grouAnagram(strs))