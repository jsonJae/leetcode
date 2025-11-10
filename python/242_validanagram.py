"""

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sHash = {}
        tHash = {}
        
        for letter in s:
            if letter not in sHash:
                sHash[letter] = 1
            sHash[letter] += 1

        for letter in t:
            if letter not in tHash:
                tHash[letter] = 1
            tHash[letter] += 1

        if sHash == tHash: return True
        return False
