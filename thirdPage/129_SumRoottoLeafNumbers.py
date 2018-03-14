class Solution:
    def travelToLeaf(self,root,path,res):
        if not root:
            return
        path+=str(root.val)
        if root.left==root.right==None:
            res.append(path)
        self.travelToLeaf(root.left,path,res)
        self.travelToLeaf(root.right,path,res)
        path=path[:-1]

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        path=""
        self.travelToLeaf(root,path,res)
        total=0
        for item in res:
            total+=int(item)
        return total

