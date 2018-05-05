class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def calculate(self,root,total,flag):
        if not root:
            return total
        if root:
            if flag and root.left is None and root.right is None:
                return total+root.val
            else:
                return self.calculate(root.left,total,True)+self.calculate(root.right,total,False)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total=0
        return self.calculate(root,total,None)




s=Solution()
print(s.sumOfLeftLeaves())