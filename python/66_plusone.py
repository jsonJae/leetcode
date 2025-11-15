"""
66. Plus One

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. The large 
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # increment the last digit
        digits[len(digits)-1] += 1

        # check if the length is 1 and the digit is equal to 100, 
        # return [1,0]
        if len(digits) == 1 and digits[0] == 10:
            digits[0] = 1
            digits.append(0)
            return digits

        #  traverse array backwards
        for i in range(len(digits)-1, 0, -1):
            # check if digit is equal to 10, then make the ith digit 0
            # and i -1 += 1
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
        
        # check if the first digit is equal to 10, make 0th element to 0
        # and insert 1 at the head
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)

        # return digits
        return digits


