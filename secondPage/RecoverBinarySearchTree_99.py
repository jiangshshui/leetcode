from createBSTFromList import createBSTFromList
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.firstNode=TreeNode(None)
        self.secondNode=TreeNode(None)
        self.preNode=TreeNode(-2**64)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.firstNode.val,self.secondNode.val=self.secondNode.val,self.firstNode.val

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        if not self.firstNode.val and self.preNode.val>=root.val:
            self.firstNode=self.preNode
        if self.firstNode.val and self.preNode.val>=root.val:
            self.secondNode=root
        self.preNode=root
        self.traverse(root.right)

class SwapTwoTreeNode():
    def __init__(self,first,second):
        self.first=first
        self.second=second
        self.firstNode=None
        self.secondNode=None
    def swap(self,root):
        # firstNode=None
        # secondNode=None
        def traverse(root, i):
            if not root:
                return i
            i=traverse(root.left, i)
            i += 1
            if i ==self.first:
                self.firstNode=root
            if i==self.second:
                self.secondNode=root
            i=traverse(root.right,i)
            return i
        traverse(root,0)
        print(self.firstNode,self.secondNode)
        self.firstNode.val,self.secondNode.val=self.secondNode.val,self.firstNode.val
        return root


s=Solution()
root=createBSTFromList([30,20,50,40,70,90,80])
print(root)
swap=SwapTwoTreeNode(3,6)
root=swap.swap(root)
print(root)
s.recoverTree(root)
print(root)