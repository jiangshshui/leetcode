from createBSTFromList import createBSTFromList
from createBSTFromList import SwapTwoTreeNode
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     preNode=None
    #     return self.traverse(root,preNode)
    #
    # def traverse(self,root,preNode):
    #     if not root:
    #         return True
    #     if not self.traverse(root.left,preNode):
    #         return False
    #     if not preNode:
    #         preNode=root
    #     if not(preNode is root) and preNode and preNode.val>root.val:
    #         return False
    #     if not self.traverse(root.right,preNode):
    #         return False
    #     return True

    def __init__(self):
        self.preNode=TreeNode(-2**64)
    def isValidBST(self,root):
        #preNode=TreeNode(-2**64)
        return self.traverse(root)

    def traverse(self,root):
        if not root:
            return True
        if not self.traverse(root.left):
            return False
        if self.preNode.val>=root.val:
            return False
        self.preNode=root
        if not self.traverse(root.right):
            return False
        return True

s=Solution()
root=createBSTFromList([1,1])
# swap=SwapTwoTreeNode(1,2)
# root=swap.swap(root)
# root=swap.swap(root)
print(s.isValidBST(root))