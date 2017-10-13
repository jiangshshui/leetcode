from createLinkListFromList import *
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head=ListNode(None)
        cur=head
        carry=0
        while l1 and l2:
            sum=l1.val+l2.val+carry
            temp=ListNode(sum%10)
            carry=sum//10
            cur.next=temp
            cur=temp
            l1=l1.next
            l2=l2.next
        if l1:
            while l1:
                sum=l1.val+carry
                temp=ListNode(sum%10)
                carry=sum//10
                cur.next=temp
                cur=temp
                l1=l1.next
        if l2:
            while l2:
                sum = l2.val + carry
                temp = ListNode(sum % 10)
                carry = sum // 10
                cur.next = temp
                cur = temp
                l2=l2.next
        if carry!=0:
            temp=ListNode(carry)
            cur.next=temp
        return head.next


myList1=createList([5])
myList2=createList([5])
s=Solution()
res=s.addTwoNumbers(myList1,myList2)
print(res)

