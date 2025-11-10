"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences 
of val in nums in-place. The order of the elements may be changed. Then 
return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements 
which are not equal to val. The remaining elements of nums are not important as 
well as the size of nums.
- Return k.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # initialize k
        k = 0  

        # traverse nums
        for i in range(len(nums)):
            # if the current number is not equal to val
            if nums[i] != val:
                # assign the current value to nums [k]
                nums[k] = nums[i]  
                # increment k
                k += 1
        # return k
        return k
