class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def isBalanced(self, root):
#         def check(root):
#             if root is None:
#                 return 0
#             left = check(root.left)
#             right = check(root.right)
#             if left == -1 or right == -1 or abs(left - right) > 1:
#                 return -1
#             return 1 + max(left, right)
#         return check(root) != -1

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
            leftHeight=self.check(root.left)
            rightHeight=self.check(root.right)
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            return 1+max(leftHeight,rightHeight)

        return check(root)!=-1

