"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize answer array to length of nums array with 1
        answer = [1] * len(nums)
        # initialized as 1 since prefix of the first num or the 
        # last num is none, so just put 1
        prefix = 1 
        postfix = 1

        # iterate over nums
        for i in range(len(nums)):
            # use the previous prefix for this (so that it will be n-1)
            answer[i] = prefix
            # update the prefix 
            prefix *= nums[i]

        # iterate over nums starting from the end to the start
        for i in range(len(nums) - 1, -1, -1):
            
            # use the previous postfix and multiply it to the answer[i] (so that it will be n+1)
            answer[i] *= postfix
            # update the prefix
            postfix *= nums[i]

        # return the answer array
        return answer

        

        