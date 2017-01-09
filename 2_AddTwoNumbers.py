# LeetCode #2 Add Two Numbers
# Dave Chang
# 2016/12/23

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = ListNode(0)
        final = current
        carry = 0
        while l1 is not None or l2 is not None or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            sum += carry
            #print sum
            carry = sum / 10
            res = sum % 10
            #print carry, res
            
            current.next = ListNode(res)
            #print current.next.val
            current = current.next
        
        #print final.next.val
        #print final.next.next.val
        #print final.next.next.next.val
        return final.next