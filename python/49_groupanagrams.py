
"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # initialize hashmap
        hashmap = {}

        # traverse every string in strs list
        for s in strs:
            # get the key by sorting s (returns a list) and joining it so that it returns a string
            key = ''.join(sorted(s))  
            # if key is not in hashmap, add a new key value pair with the key and a list containing the current string
            if key not in hashmap:
                hashmap[key] = [s]
            # otherwise, append the current string to the value of the key which is a list
            else:
                hashmap[key].append(s)

        # return list of list of strings
        return list(hashmap.values())
