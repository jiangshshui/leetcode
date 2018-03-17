class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        res=[]
        while self:
            res.append(self.val)
            self=self.next
        return str(res)

class Solution(object):
    def split(self,head):
        walker=head
        runner=head
        while runner and runner.next and runner.next:
            walker=walker.next
            runner=runner.next.next
        return walker

    def reverse(self,head):
        new_head=ListNode(0)
        while head:
            cache=head.next
            head.next=new_head.next
            new_head.next=head
            head=cache
        return new_head.next
    def meger_two_list(self,head,right_begin):
        if head is right_begin:
            return
        new_head=ListNode(0)
        work_new_head=new_head
        while right_begin:
            cache_head=head.next
            cache_right=right_begin.next
            work_new_head.next=head
            work_new_head.next.next=right_begin
            work_new_head=work_new_head.next.next
            head=cache_head
            right_begin=cache_right
            if head is right_begin:
                break
        return new_head.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        right_begin=self.split(head)
        reverse_right_begin=self.reverse(right_begin)
        res=self.meger_two_list(head,reverse_right_begin)

def creatList(n):
    cur=head=ListNode(0)
    for i in range(1,n+1):
        newNode=ListNode(i)
        newNode.next=None
        cur.next=newNode
        cur=cur.next
    return head.next

l1=creatList(6)
print(l1)
s=Solution()
s.reorderList(l1)
print(l1)


