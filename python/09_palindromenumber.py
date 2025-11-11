"""
9. Palindrome Number    

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # convert the number to string
        num = str(x)

        # traverse the string
        for i in range(len(num)):
                # check if the ith element and the ith element from the last not equal
                if num[i] != num[len(num) - (i+1)]:
                    # return false if not the same, else return true
                    return False
        return True