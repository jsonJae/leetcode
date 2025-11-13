"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # check if the length of the array is 0 or 1
        # return accordingly since it is the longest
        # consecutive sequence
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        lcs = 1
        curr = 1

        # sort the array first
        nums.sort()
        
        # iterate over the nums except the last element
        # since we are checking the ith and i+1th element 
        # every iteration
        for i in range(len(nums)-1):
            # check if the previous element incremented by 1 is 
            # equal to next element
            if nums[i] + 1 == nums[i+1]:
                # increment the curr value
                curr += 1
            else:
                # check if i and i+1 elements are equal, if not
                # reinitialize curr to 1
                if nums[i] != nums[i+1]:
                    curr = 1
            
            # check if curr is greater than lcs, if yes
            # store the current longest sequence to lcs
            if curr > lcs:
                lcs = curr
        return lcs

        
                

            
        