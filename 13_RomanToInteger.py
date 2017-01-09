# LeetCode #13  Roman to Integer
# Dave Chang
# 2017/01/01

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # rule to convert roman numeral to integer
        # when one is larger/equal than its latter one, it's added
        # when one is less than its latter one, it's subtracted
        # last one is always added
        
        romanNumeral = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        finalSum = 0
        for i in xrange(0, len(s)-1):
            if romanNumeral[s[i]] >= romanNumeral[s[i+1]]:
                finalSum += romanNumeral[s[i]]
            else:
                finalSum -= romanNumeral[s[i]]
        # Need to add the last one
        finalSum += romanNumeral[s[-1]]
        
        return finalSum