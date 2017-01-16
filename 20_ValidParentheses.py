# LeetCode #20 Valid Parentheses
# Dave Chang
# 2017/01/15


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")":"(", "]":"[", "}":"{"}
        temp = []
        
        for i in s:
            if i in dict.values():
                temp.append(i)
            elif i in dict and len(temp) != 0:
                if temp.pop() != dict[i] :
                    return False
                    break
                else:
                    continue
            # not even parenthese or first one is }])
            else:
                return False
        return len(temp) == 0