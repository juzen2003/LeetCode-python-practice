# LeetCode #14 Longest Common Prefix
# Dave Chang
# 2017/01/02


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #empty list 
        if strs == []:
            return ""
        
        temp = ""
        s = strs[0]
        minLength = len(s)
        isCommon = True
        
        # get the minimum length of string to reduce the search
        for item in strs:
            minLength = min(minLength, len(item))
        
        if minLength == 0:
            return ""
        
        for i in xrange(0, minLength):
            for item in strs:
                if s[i] == item[i]:
                    continue
                else:
                    isCommon = False
            if isCommon:
                temp += s[i]
        return temp
                    