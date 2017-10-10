class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return "".join(str(res))

def createLinkFromList(nums):
    head=cur=ListNode(None)
    for item in nums:
        cur.next=ListNode(item)
        cur=cur.next
    return head.next

class Solution(object):
    def partition(self, head, x):
        lessList=lessCur=ListNode(None)
        greaterList=greaterCur=ListNode(None)
        cur=head
        if head is None:
            return head
        while cur:
            if cur.val>x:
                #greaterCur.next=ListNode(cur.val)
                greaterCur.next = cur
                greaterCur=greaterCur.next
            else:
                # lessCur.next=ListNode(cur.val)
                lessCur.next = cur
                lessCur=lessCur.next
            cur=cur.next
        greaterCur=None
        lessCur.next=greaterList.next
        return lessList.next

s=Solution()
l=createLinkFromList([2,1])
print(l)
res=s.partition(l,2)
print(res)


