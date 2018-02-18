class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.datas=[]
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            self.datas.append(root.val)
            traverse(root.right)
        traverse(root)
        m={}
        for data in self.datas:
            if data not in m:
                m[data]=1
            else:
                m[data]+=1
        maximum=0
        for key in m.keys():
            if maximum<m[key]:
                maximum=m[key]
        res=[]
        for key in m.keys():
            if maximum==m[key]:
                res.append(key)
        return key


