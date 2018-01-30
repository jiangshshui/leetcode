class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from  createLinkListFromList import createList
class Solution(object):
    def removeElements(self, head, val):
        cur=head
        pre=ListNode(0)
        pre.next=cur
        newHead=pre
        while cur:
            if cur.val==val:
                cur=cur.next
                pre.next=cur
                continue
            else:
                pre=pre.next
                cur=cur.next
        return newHead.next
        #return head

link=createList([1,2,6,3,4,5,6])
print(Solution().removeElements(link,6))