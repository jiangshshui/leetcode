class Solution:

    def calcDepth(self,root,depth,res):
        # if not root:
        #     return
        if root.left==root.right==None:
            res.append(depth)
            return
        if root.left:
            self.calcDepth(root.left,depth+1,res)
        if root.right:
            self.calcDepth(root.right,depth+1,res)


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return False
        res=[]
        self.calcDepth(root,1,res)
        return max(res)
