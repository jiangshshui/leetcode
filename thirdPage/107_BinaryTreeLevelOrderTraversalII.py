from queue import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        q=Queue()
        q.put((root,1))
        prelevel=1
        temp=[]
        while not q.empty():
            node,level=q.get()
            if prelevel<level:
                res.append(temp)
                temp=[]
                prelevel=level
                temp.append(node.val)
            else:
                temp.append(node.val)
            if node.left:
                q.put((node.left,level+1))
            if node.right:
                q.put((node.right,level+1))
        if len(temp)!=0:
            res.append(temp)
        return res[::-1]

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

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    def readlines():
        yield sys.stdin.readline()

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            ret = Solution().levelOrderBottom(root)
            print(ret)
            #out = treeNodeToString(root)
            # if ret is not None:
            #     print("Do not return anything, modify root in-place instead.")
            # else:
            #print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
# [3,9,20,null,null,15,7]