class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSumFrom(self,node,sum):
        if not node:
            return 0
        return (1 if node.val==sum else 0)+self.pathSumFrom(node.left,sum-node.val)+\
               self.pathSumFrom(node.right,sum-node.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)