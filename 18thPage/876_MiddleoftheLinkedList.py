class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oneStep=head
        twoStep=head
        while twoStep.next:
            oneStep=oneStep.next
            if twoStep.next.next:
                twoStep=twoStep.next.next
            elif twoStep.next:
                twoStep=twoStep.next
        res=[]
        while oneStep:
            res.append(oneStep.val)
            oneStep=oneStep.next
        return res



