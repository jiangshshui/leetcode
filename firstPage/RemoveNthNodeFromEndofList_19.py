from createLinkListFromList import *


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if n<=0:
            return head
        newHead=ListNode(None)
        newHead.next=head
        head=newHead
        pre=head
        cur=head.next
        i=0
        while cur:
            cur=cur.next
            i+=1
            if i>n:
                pre=pre.next
        pre.next=pre.next.next
        return head.next

list=createList([1,2,3,4,5])
s=Solution()
print(s.removeNthFromEnd(list,2))
