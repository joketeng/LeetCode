# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#       self.val = x
#       self.next = None
       
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry%10)
            prev = prev.next
            carry = carry//10
        return result.next