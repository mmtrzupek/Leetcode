# 49. Group Anagrams (Medium)

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    if len(strs) == 0:
        return [[""]]
    
    ans = []
    d = {}

    for i in range(len(strs)):
        s = ""
        s = ''.join([str(item) for item in sorted(strs[i])])

        if s not in d:
            d[s] = []
            d[s].append(strs[i])
        else:
            d[s].append(strs[i])
    
    for k, v in d.items():
        ans.append(v)

    return ans


