class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

def transfer(s1):
    root=n=ListNode(0)
    for i in s1.split(' '):
        temp=ListNode(int(i))
        n.next=temp
        n=n.next
    return root.next


def printList(temp):
    while (temp):
        print(temp.val,end=' ')
        temp = temp.next
    print()
if __name__=='__main__':
    s1=input("请输入list1(以空格为分隔符):")
    l1=transfer(s1)
    s2=input("请输入list2(以空格为分隔符):")
    l2=transfer(s2)
    printList(l1)
    printList(l2)
    s=Solution()
    res=s.addTwoNumbers(l1,l2)
    printList(res)