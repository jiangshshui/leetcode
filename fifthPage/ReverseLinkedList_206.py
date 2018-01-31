class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead=ListNode(-1)
        while head:
            temp=head.next
            head.next=newHead.next
            newHead.next=head
            head=temp
        return newHead.next

