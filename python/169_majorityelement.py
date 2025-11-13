"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume 
that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize empty hashmap
        hashmap = {}
        # get length of numes
        num_length = len(nums)

        # traverse the nums array
        for num in nums:
            # if key is not in the hashmap, add the key 
            # to the hashmap and initialize the value to 1
            if num not in hashmap:
                hashmap[num] = 1
            # else, if it's in the hashmap, increment the value
            else:
                hashmap[num] += 1

        # iterate over the keys in hashmap and check if their
        # value is greater than num_length/2
        for key in hashmap:
            if hashmap[key] > num_length/2:
                return key