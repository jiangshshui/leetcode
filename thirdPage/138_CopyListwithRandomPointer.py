class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur=head
        #复制LinkList上的节点
        while cur:
            copy=RandomListNode(cur.label)
            cur_next=cur.next
            cur.next=copy
            copy.next=cur_next
            cur=cur_next

        cur=head
        while cur:
            copy=cur.next
            random=cur.random#原先的指向
            if random:
                copy.random=random.next
            else:
                copy.random=random
            cur=cur.next.next

        newHead=RandomListNode(0)
        cur=newHead#生成新的list
        cur_iter=head#迭代原先的list

        while cur_iter:
            copy=cur_iter.next
            cur_iter.next=copy.next
            cur.next=copy
            cur=cur.next
            cur_iter=cur_iter.next

        return newHead.next
s=Solution()
print(s.copyRandomList())