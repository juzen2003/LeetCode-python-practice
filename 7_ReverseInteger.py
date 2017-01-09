# LeetCode #7 Reverse Integer
# Dave Chang
# 2016/12/27


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversedX = 0
        isNegative = False
        
        if x < 10 and x > -10:
            return x
        elif x >= 10 or x <= -10:
            if x < 0:
                x *= -1
                isNegative = True
            while x != 0:
                mod = x % 10
                x = x / 10
                reversedX = reversedX * 10 + mod
            if isNegative:
                reversedX *= -1
            # overflow case
            if reversedX > 2147483647 or reversedX < -2147483647:
                return 0
            else:
                return reversedX