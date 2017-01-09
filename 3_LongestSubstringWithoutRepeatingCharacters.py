# LeetCode #3 Longest Substaing Without Repeating Characters
# Dave Chang
# 2016/12/25

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this is to store existing char from the s (key:value -> s[index]: index)
        temp = {}
        currentMax = 0
        checkPoint = 0
        
        for i in xrange(len(s)):
            if s[i] not in temp:
                #temp[s[i]] = i
                currentMax = max(currentMax, i-checkPoint+1)
            elif s[i] in temp:
                if temp[s[i]] >= checkPoint:
                    checkPoint = temp[s[i]] + 1
                    currentMax = max(currentMax, i-checkPoint+1)
                    #temp[s[i]] = i
                else:
                    currentMax = max(currentMax, i-checkPoint+1)
                    #temp[s[i]] = i
            temp[s[i]] = i
        
        '''
        for i in xrange(len(s)):
            if s[i] in temp and temp[s[i]] >= checkPoint:
                checkPoint = temp[s[i]] + 1
            currentMax = max(currentMax, i-checkPoint+1)
            temp[s[i]] = i
        '''
        
        return currentMax