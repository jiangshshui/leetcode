from  createLinkListFromList import *
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        newHead=ListNode(None)
        #head=newHead
        newHead.next=head
        head=newHead
        pre=head
        while pre:
            if pre.next and pre.next.next:
                mid=pre.next
                last=pre.next.next
                pre.next=last
                mid.next=last.next
                last.next=mid
                pre=pre.next.next
            else:
                break
        return head.next
s=Solution()
mylist=createList([])
print(s.swapPairs(mylist))

