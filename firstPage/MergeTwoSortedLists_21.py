class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp=root=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=cur=l1
                l1=l1.next
            else:
                temp.next=cur=l2
                l2=l2.next
            temp=cur
        if l1:
            while l1:
                temp.next = cur=l1
                l1=l1.next
                temp=cur
        if l2:
            while l2:
                temp.next = cur=l2
                l2=l2.next
                temp=cur
        return root.next



def createList(start,end,step=1):
    root=temp=cur=ListNode(0)
    for x in range(start,end,step):
        cur=ListNode(x)
        temp.next=cur
        temp=cur
    return root.next


def printList(list):
    while list:
        print(list.val,end=' ')
        list=list.next

l1=createList(2,2)
l2=createList(1,1)

s=Solution()
res=s.mergeTwoLists(l1,l2)
printList(res)


