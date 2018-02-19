class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=0
        m={}
        def traverse(root,level):
            if root is None:
                return
            traverse(root.left,level+1)
            if level not in m:
                m[level] = root.val
            traverse(root.right,level+1)
        traverse(root,1)
        maximum=max(m.keys())
        return m[maximum]

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
        while True:
            yield sys.stdin.readline().strip("\n")

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            ret = Solution().findBottomLeftValue(root)
            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
# s=Solution()
# print(s.findBottomLeftValue())


# [1,2,3,4,null,5,6,null,null,7]
#[2,1,3]