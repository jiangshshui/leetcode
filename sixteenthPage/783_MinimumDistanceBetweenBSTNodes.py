class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    pre = -float("inf")
    minimum = float("inf")
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)
        self.minimum=min(root.val-self.pre,self.minimum)
        self.pre=root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.minimum
# s=Solution()
# print(s.minDiffInBST())

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
        yield sys.stdin.readline()

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            ret = Solution().minDiffInBST(root)
            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()