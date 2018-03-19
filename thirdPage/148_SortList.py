import json
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def split(self,head,n):
        i=1
        while i<n and head:
            i+=1
            head=head.next
        if not head:
            return None
        second=head.next
        head.next=None
        return second

    def merge(self,l1,l2,head):
        cur=head
        while l1 and l2:
            if l1.val>l2.val:
                cur.next=l2
                cur=l2
                l2=l2.next
            else:
                cur.next=l1
                cur=l1
                l1=l1.next
        cur.next=(l1 if l1 else l2)
        while cur.next:
            cur=cur.next
        return cur
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        length=0
        cur=head
        while cur:
            length+=1
            cur=cur.next
        dummy=ListNode(0)
        dummy.next=head
        step=1
        while step<length:
            cur=dummy.next
            tail=dummy
            while cur:
                left=cur
                right=self.split(left,step)
                cur=self.split(right,step)
                tail=self.merge(left,right,tail)
            step*=2
        return dummy.next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        # for line in sys.stdin:
        #     yield line.strip('\n')
        yield sys.stdin.readline()

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            ret = Solution().sortList(head)
            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()


'''
[1,23,4,6,7,90,50]
[23,1,4,2,789,90,50]
'''