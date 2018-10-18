# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(None)
        result.next = head
        prev = result
        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = node1.next
            lat = node2.next
            prev.next = node2
            node2.next = node1
            node1.next = lat
            prev = node1
        return result.next






# ·¨¶þ


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = node1.next
            prev.next, node2.next, node1.next = node2, node1, node2.next
            prev = node1
        return self.next

