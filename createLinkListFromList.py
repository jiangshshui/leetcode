class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res=[]
        while self:
            res.append(str(self.val))
            self=self.next
        return "".join(res)

def createList(l):
    head=cur=ListNode(None)
    for i in l:
        cur.next=ListNode(i)
        cur=cur.next
    return head.next
