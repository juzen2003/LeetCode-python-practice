# LeetCode #9 Palindrome Number
# Dave Chang
# 2016/12/30

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        # negative number can't be palindrome number, so no need to get rid of the signed
        #if temp[0] in ["+","-"]:
        #    temp = temp[1::]
        if temp == temp[::-1]:
            return True
        else:
            return False