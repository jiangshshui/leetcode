class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total=0
        def traverseBST(root):
            if not root:
                return
            traverseBST(root.right)
            root.val+=self.total
            self.total=root.val
            traverseBST(root.left)
        traverseBST(root)
        return root