# LeetCode #19 Remove Nth Node From End of List  
# Dave Chang
# 2017/01/08

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        final = current
        temp = None
        count = 1
        length = 1
        # get the length of linked list & the whole linked list
        while head.next != None:
            length += 1
            head = head.next
        #print "Length: ", length
        #print "Node 1 Value: ", current.val
        #print "Node 2 Value: ", current.next.val
        #print "Node 3 Value: ", current.next.next.val
       
        while count <= length:
            #print "Value: ", current.val
            if length == n:
                temp = current.next
                final = temp
            else:
                if count == (length - n):
                    temp = current.next
                    current.next = temp.next
                else:
                    current = current.next
            count += 1    
        
        return final