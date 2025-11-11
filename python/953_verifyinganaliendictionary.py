"""
In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation 
of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien
language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # initialize a hashmap
        hashmap = {}

        #store the characters and rtheir corresponding index in the hashmap
        for i in range(len(order)):
            hashmap[order[i]] = i

        print(hashmap)
        # traverse the words in the array (but dont include the last character 
        #since it will bve xomputed in the second to the last iteration)
        for i in range(len(words)-1):
            # traverse length of word[i]
            for j in range(len(words[i])):
                # check if the next word is a prefix of the current word
                if j >= len(words[i+1]):
                    return False
                # if the current element of current and next word is the same
                if words[i][j] != words[i+1][j]:
                    # check if the letter of the current word is greater than the 
                    # next number 
                    if hashmap[words[i][j]] > hashmap[words[i+1][j]]:
                        return False
                    # if false go to the next word
                    else:
                        break
        # return true if the conditions are not met                    
        return True


