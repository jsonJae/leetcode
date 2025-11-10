"""
01. Two Sums

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.You may assume that each input would 
have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initialize a hashmap
        hashmap = {}   
        i = 0
    
        # iterate nums array 
        while i < len(nums): 
            # get the complement of the target
            complement = target - nums[i]
            
            # check if the complement is already in hashmap
            if complement in hashmap:
                # return an array containing the index of the complement and index of the current number
                return [hashmap[complement], i]
            
            # else add the current number as key and its index as the value
            hashmap[nums[i]] = i
            i += 1 
        # return empty array if there are no numbers that sums to target 

# time complexity = O(n)