# LeetCode #21 Merge Two Sorted Lists
# Dave Chang
# 2017/01/15

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = ListNode(x=0)
        final = current
        
        # from small number to big number
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        
        if l1 is None:
            current.next = l2
        elif l2 is None:
            current.next = l1
        
        return final.next