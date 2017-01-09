# LeetCode #8 String to Integer (atoi)
# Dave Chang
# 2016/12/29


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = ""
        final = None
        i = 0
        ov_max = 2147483647
        ov_min = -2147483648
        str = str.strip()
        
        if len(str) == 0:
            return 0
        if str[0] in ["+", "-"]:
            i = 1
            temp += str[0]
        
        for i in xrange(i, len(str)):
            if str[i].isdigit():
                temp += str[i]
                continue
            else:
                break
        try:
            final = int(temp)
        except:
            return 0
        else:
            if final > ov_max:
                return ov_max
            elif final < ov_min:
                return ov_min
            else:
                return final