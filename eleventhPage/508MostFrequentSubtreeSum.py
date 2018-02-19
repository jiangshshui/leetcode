# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # def calcSum(root):
        #     if root is None:
        #         return 0
        #     lsum=calcSum(root.left)
        #     rsum=calcSum(root.right)
        #     return lsum+rsum+root.val

        m={}
        def traverse(root):
            if root is None:
                return 0
            lsum=traverse(root.left)
            rsum=traverse(root.right)
            total=lsum+rsum+root.val
            if total not in m:
                m[total]=1
            else:
                m[total]+=1
            return total
        traverse(root)
        res=[]
        if len(m)==0:
            return []
        maximum=max(m.values())
        for key in m.keys():
            if m[key]==maximum:
                res.append(key)
        return res

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
        # for line in sys.stdin.readline():
        #     yield line.strip('\n')
        # for line in sys.stdin:
        #     yield line.strip('\n')
        while True:
            line=sys.stdin.readline()
            yield line.strip('\n')
        # line=sys.stdin.readline()
        # yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            ret = Solution().findFrequentTreeSum(root)
            # out = intToString(ret)
            # print(out)
            print(ret)
        except StopIteration:
            break

if __name__ == '__main__':
    main()


#[5,2,-3]
#[5,2,-5]

# s=Solution()
# print(s.findFrequentTreeSum(root))