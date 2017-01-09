# LeetCode #1 Two Sum
# Dave Chang
# 2016/12/20

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            firstNum = nums[i]
            secondNum = target - firstNum
            if secondNum in nums and i != nums.index(secondNum):
                if i > nums.index(secondNum):
                    return [nums.index(secondNum), i]
                return [i, nums.index(secondNum)]
            
            
#sol = Solution()
#sol.twoSum(nums=[3,2,4],target=6)
