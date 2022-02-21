# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            middle = (l + r) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                r = middle - 1
            else:
                l = middle + 1