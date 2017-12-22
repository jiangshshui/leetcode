from queue import PriorityQueue
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __le__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

from queue import PriorityQueue
import json
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                 q.put((cur.next.val,cur.next))
        return dummy.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)
    # Now convert that list into linked list
    dummyRoot = ListNode(None)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


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
        for line in sys.stdin.readlines():
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            #line = lines.next()
            line=next(lines)
            if line=="":
                break
            lists = stringToListNodeArray(line)
            ret = Solution().mergeKLists(lists)
            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()