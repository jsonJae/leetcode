"""
Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # initialize empty hashmap
        hashmap = {}

        # traverse nums
        for i in range(len(nums)):
            # if nums[i] is already in hashmap return true
            if nums[i] in hashmap:
                return True
            # else add the number and its index to the tail of the hashmap
            hashmap[nums[i]] = i

            # check if the length of the hashmap is greater than k 
            if len(hashmap) > k:
                # remove the number at the head of the Hashmap
                hashmap.pop(nums[i-k])
            
        return False
                
        