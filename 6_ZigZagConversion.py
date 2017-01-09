# LeetCode #6 ZigZag Conversion
# Dave Chang
# 2016/12/26

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        newString = ""
        space = 2*numRows - 2
        for i in xrange(numRows):
            # these are cased when we can just return the string
            if numRows >= len(s) or numRows == 1:
                return s
            elif i == 0 or i == numRows-1:
                index = i
                while (index) < len(s):
                    newString = newString + s[index]
                    index += space
                     
            else:
                index = i
                midIndex = space - i
                while (index) < len(s):
                    newString = newString + s[index]
                    if (midIndex) < len(s):
                        newString = newString + s[midIndex]
                        midIndex += space
                    index += space
        return newString