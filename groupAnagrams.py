"""
Given an array of strings strs, group the anagrams together.

Example 1:
strs = ["eat","tea","tan","ate","nat","bat"]
return [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from collections import defaultdict

def groupAnagrams(strs):
    
    dct = defaultdict(list)
    
    for word in strs:
        dct(tuple(sorted(word))).append(word)
        
    return dct.values()


