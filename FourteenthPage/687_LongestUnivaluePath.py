from queue import Queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        self.res=0
        def helper(node,parent):
            if not node:
                return 0
            left=helper(node.left,node)
            right=helper(node.right,node)
            left=left+1 if(node.left and node.val==node.left.val) else 0
            right=right+1 if(node.right and node.val==node.right.val) else 0
            self.res=max(self.res,left+right)
            return max(left,right)
        helper(root,root)
        return self.res


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None
    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1
        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
        if index >= len(inputValues):
            break
        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def intToString(input):
    if input is None:
        input = 0
    return str(input)


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
            root = stringToTreeNode(line)
            ret = Solution().longestUnivaluePath(root)
            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__=="__main__":
    main()