class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        walker=head
        runner=head
        while runner.next and runner.next.next:
            walker=walker.next
            runner=runner.next.next
            if walker==runner:
                walker=head
                while walker!=runner:
                    walker=walker.next
                    runner=runner.next
                return walker
        return None



s=Solution()
print(s.detectCycle())