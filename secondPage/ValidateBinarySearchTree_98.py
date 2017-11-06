from createBSTFromList import createBSTFromList
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        preNode=None
        return self.traverse(root,preNode)

    def traverse(self,root,preNode):
        if not root:
            return True
        if not self.traverse(root.left,preNode):
            return False
        if not preNode:
            preNode=root
        if not preNode and preNode.val>root.val:
            return False
        if not self.traverse(root.right,preNode):
            return False
        return True

s=Solution()
root=createBSTFromList([1,2])

print(s.isValidBST(root))