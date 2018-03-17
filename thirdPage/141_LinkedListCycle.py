class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        walker=head
        runner=head
        while runner.next and runner.next.next:
            walker=walker.next
            runner=runner.next.next
            if walker==runner:
                return True
        return False

s=Solution()
print(s.hasCycle())

'''
http://www.cnblogs.com/wuyuegb2312/p/3183214.html
解释
'''