class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        pre=False  #前面的单词是否是一个linked list中的
        work=head
        res=0
        G=set(G)
        while work:
            if work.val in G:
                # index=G.index(work.val)
                # del(G[index])
                G.remove(work.val)
                pre=True
                if work.next is None:
                    res+=1
            else:
                if pre:
                    res+=1
                    pre=False
            work=work.next
        return res

import json
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


def main():
    import sys
    def readlines():
        # for line in sys.stdin.readline():
        #     yield line.strip('\n')
        while True:
            yield sys.stdin.readline()

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)
            line = next(lines)
            G = stringToIntegerList(line)

            ret = Solution().numComponents(head, G)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__=="__main__":
    main()